import hashlib
import sys
from cryptography.fernet import Fernet
import os
import shutil
import pathlib

aoc_decript_var = "AOC_DECRYPT_KEY"


def write_key():
    """
    Generates a key and save it into a file
    """
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)


# write_key()


def load_key_from_env():
    """
    Loads the key from the current environment
    """
    key = os.getenv(aoc_decript_var)

    return key

def load_key_from_dotenv():
    """
    Loads the key from the .env file
    """
    if os.path.isfile(".env"):
        with open(".env", "r") as env_file:
            lines = env_file.readlines()

            for line in lines:
                if aoc_decript_var in line:
                    return line.strip()[len(aoc_decript_var) + 1 :]

    return None

def load_key():
    key = load_key_from_env()

    if key is None:
        print("Encryption key is missing in environment.")
        print("Trying from .env file.")

        key = load_key_from_dotenv()

        if key is None:
            print("Encryption key not found in .env file")
            raise Exception("Key not found")
    
    return key

def remove_tmp_from_name(filename: str):
    abs_filename = str(pathlib.Path.absolute(pathlib.Path(filename)))

    name, _ = abs_filename.split(".")

    return f"{name[:-4]}"



def encrypt(filename, key):
    """
    Given a filename (str) and key (bytes), it encrypts the file and write it
    """
    f = Fernet(key)

    with open(filename, "rb") as file:
        # read all file data
        file_data = file.read()

        # encrypt data
    encrypted_data = f.encrypt(file_data)

    new_filename = remove_tmp_from_name(filename)

    # write the encrypted file
    with open(new_filename, "wb") as file:
        file.write(encrypted_data)



def calculate_file_hash(file_path):
    with open(file_path, "rb") as f:
        file_hash = hashlib.sha256(f.read()).hexdigest()
    return file_hash

def main():
    key: str
    try:
        key = load_key()
    except Exception:
        print("Error: Encryption key not found")
        sys.exit(1);
    
    
    answers_hash_old = None
    try:
        with open("./data/answers.hash", 'r') as f:
            lines = f.readlines();
            if len(lines) != 1:
                raise Exception("Incorrect hash file")
            
            answers_hash_old = lines[0]
    except Exception:
        pass    
    
    input_hash_old = None
    try:
        with open("./data/input.hash", 'r') as f:
            lines = f.readlines();
            if len(lines) != 1:
                raise Exception("Incorrect hash file")
            
            input_hash_old = lines[0]
    except Exception:
        pass 

    
    print("answers_hash_old:", answers_hash_old)
    print("  input_hash_old:", input_hash_old)

    shutil.make_archive("./data/answers_tmp", "zip", "./answers")
    shutil.make_archive("./data/input_tmp", "zip", "./input")

    answers_hash = calculate_file_hash("./data/answers_tmp.zip")
    input_hash = calculate_file_hash("./data/input_tmp.zip")
    
    print("answers_hash:", answers_hash)
    print("  input_hash:", input_hash)

    if answers_hash != answers_hash_old:
        print("New answers")
        encrypt("./data/answers_tmp.zip", key)
        with open("./data/answers.hash" , 'w') as f:
            f.write(answers_hash)

    if input_hash != input_hash_old:
        print("New inputs")
        encrypt("./data/input_tmp.zip", key)
        with open("./data/input.hash" , 'w') as f:
            f.write(input_hash)

    os.remove("./data/answers_tmp.zip")
    os.remove("./data/input_tmp.zip")

    # encrypt("answers.zip", key)
    # decrypt("answers.zip", key)


if __name__ == "__main__":
    main()
