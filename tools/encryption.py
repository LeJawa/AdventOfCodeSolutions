from cryptography.fernet import Fernet
import os

AOC_DECRIPT_VAR = "AOC_DECRYPT_KEY"


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
    key = os.getenv(AOC_DECRIPT_VAR)

    return key


def load_key_from_dotenv():
    """
    Loads the key from the .env file
    """
    if os.path.isfile(".env"):
        with open(".env", "r") as env_file:
            lines = env_file.readlines()

            for line in lines:
                if AOC_DECRIPT_VAR in line:
                    return line.strip()[len(AOC_DECRIPT_VAR) + 1:]

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


key = None


def encrypt(contents: bytes):
    global key

    if key == None:
        key = load_key()

    f = Fernet(key)

    encrypted_data = f.encrypt(contents)

    return encrypted_data


def decrypt(contents: bytes):
    global key

    if key == None:
        key = load_key()

    f = Fernet(key)

    decrypted_data = f.decrypt(contents)

    return decrypted_data
