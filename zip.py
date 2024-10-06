import os
import zipfile

# shutil.make_archive("./answers", "zip", "./answers")
# shutil.unpack_archive("./answers.zip", ".", "zip")

with zipfile.ZipFile("./answers.zip") as zip:
    file_names = zip.namelist()
    print(file_names)
    
    directory = "./answers"

    all_files = []
    for root, dirs, files in os.walk(directory):
        if root == directory:
            continue
        # all_files.append(root + "/")
        for file in files:
            all_files.append(os.path.join(root, file))

    # Removes root dir from files and replaces \\ by /
    clean_files = [f[len(directory)+1:].replace("\\", "/") for f in all_files]

    for f in clean_files:
        if f not in file_names:
            # add this file to zip
            pass
        else:
            # Check equality
            with open(os.path.join(directory, f), "rb") as file:
                zip_contents =  zip.read(f)
                contents = file.read()
                
                if contents != zip_contents:
                    print("Discrepancy!", f)
                    print("Zipfile:")
                    print(zip_contents.decode("utf-8"))
                    print("Current:")
                    print(contents.decode("utf-8"))