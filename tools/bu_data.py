import os
import sys
import io
import zipfile

from tools.encryption import decrypt, encrypt

ANSWERS_DATA_FILE = "data/answers"
INPUT_DATA_FILE = "data/input"

ANSWERS_DIR = "./answers"
INPUT_DIR = "./input"

DATA_DIR = "./data"
DIRS_TO_BACKUP = ["./answers", "./input"]

BU_SUFFIX = "__BU__"


def main(args):
    force_merge = False

    if ("--force" in args):
        force_merge = True

    for dir in DIRS_TO_BACKUP:
        filename = get_data_filename_from_dir(dir);
        zip_data(filename, dir, force_merge)


def get_data_filename_from_dir(reldir: str) -> str:
    filename = reldir.replace("\\", "/")

    if reldir.startswith("./"):
        filename = os.path.join(DATA_DIR, reldir[2:])
    if reldir.endswith("/"):
        filename = filename[:-1]

    return filename

def merge_bu_data_into_current(filename, target_dir):
    has_conflicts = False

    if not os.path.isfile(filename):
        error = FileNotFoundError()
        error.filename = filename
        raise error

    print(f"Opening encrypted file ({filename})...")

    with open(filename, "rb") as encrypted_file:
        zip_contents = decrypt(encrypted_file.read())

    print(f"Merging backed-up files with current files...")

    with zipfile.ZipFile(io.BytesIO(zip_contents), "r") as zip:
        file_names = zip.namelist()
        # print(file_names)

        all_files = []
        for root, dirs, files in os.walk(target_dir):
            if root == target_dir:
                continue
            # all_files.append(root + "/")
            for file in files:
                all_files.append(os.path.join(root, file))

        # Removes root dir from files and replaces \\ by /
        clean_files = [f[len(target_dir)+1:].replace("\\", "/")
                       for f in all_files]

        for f in file_names:
            filepath = os.path.join(target_dir, f)
            os.makedirs(os.path.dirname(filepath), exist_ok=True)

            if f not in clean_files:
                # add this file to target_dir
                zip_contents = zip.read(f)
                with open(filepath, "wb") as new_file:
                    new_file.write(zip_contents)

            else:
                # Check equality
                with open(filepath, "rb") as file:
                    zip_contents = zip.read(f)
                    contents = file.read()

                    if contents != zip_contents:
                        print("Discrepancy!", f)
                        with open(filepath + BU_SUFFIX, "wb") as new_file:
                            new_file.write(zip_contents)
                        has_conflicts = True

    return has_conflicts


def zip_data(filename, target_dir, force_merge: bool):
    has_conflicts = False

    if not force_merge:
        try:
            has_conflicts = merge_bu_data_into_current(filename, target_dir)
        except FileNotFoundError as e:
            print(f"Couldn't find the following file: {e.filename}")

    if force_merge or not has_conflicts:

        print(f"Creating encrypted file with current files...")

        zip_buffer = io.BytesIO()

        with zipfile.ZipFile(zip_buffer, "w") as zfile:
            for root, dirs, files in os.walk(target_dir):
                for file in files:
                    file_path = os.path.join(root, file)
                    arcname = os.path.relpath(file_path, start=target_dir)
                    zfile.write(file_path, arcname)

        zip_buffer.seek(0)
        zip_data = zip_buffer.read()

        os.makedirs(os.path.dirname(filename), exist_ok=True)

        with open(filename, "wb") as encypted_file:
            encypted_file.write(encrypt(zip_data))

        print("Success!")


def list_files(file: str):
    with open(file, "rb") as encrypted_file:
        zip_contents = decrypt(encrypted_file.read())

    with zipfile.ZipFile(io.BytesIO(zip_contents), "r") as zip:
        file_names = zip.namelist()
        print(file_names)


if __name__ == "__main__":
    main(sys.argv[1:])
