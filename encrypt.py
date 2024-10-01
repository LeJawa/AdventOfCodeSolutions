import sys
from cryptography.fernet import Fernet
import os

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
                    return line.strip()[len(aoc_decript_var)+1:]
    
    return None


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

    # write the encrypted file
    with open(filename, "wb") as file:
        file.write(encrypted_data)

def decrypt(filename, key):
    """
    Given a filename (str) and key (bytes), it decrypts the file and write it
    """
    f = Fernet(key)
    with open(filename, "rb") as file:
        # read the encrypted data
        encrypted_data = file.read()
    # decrypt data
    decrypted_data = f.decrypt(encrypted_data)
    # write the original file
    with open(filename, "wb") as file:
        file.write(decrypted_data)


def main():
    key = load_key_from_env()

    if key is None:
        print("Encryption key is missing in environment.")
        print("Trying from .env file.")

        key = load_key_from_dotenv()

        if key is None:
            print("Encryption key not found in .env file")
            print("Aborting")
            sys.exit(1)


    # encrypt("test.txt", key)
    # decrypt("test.txt", key)


main()