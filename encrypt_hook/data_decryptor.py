import os
import pathlib
import shutil
import sys
from data_encryptor import calculate_file_hash, load_key
from cryptography.fernet import Fernet


def decrypt(filename, key):
    """
    Given a filename (str) and key (bytes), it decrypts the file and writes it
    """
    f = Fernet(key)
    with open(filename, "rb") as file:
        # read the encrypted data
        encrypted_data = file.read()
    # decrypt data
    decrypted_data = f.decrypt(encrypted_data)
    # write the original file
    with open(filename + "_tmp.zip", "wb") as file:
        file.write(decrypted_data)




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

    answers_hash = None
    input_hash = None

    if os.path.isdir("./input"):
        shutil.make_archive("./data/answers_tmp", "zip", "./answers")
        answers_hash = calculate_file_hash("./data/answers_tmp.zip")
    if os.path.isdir("./input"):
        shutil.make_archive("./data/input_tmp", "zip", "./input")
        input_hash = calculate_file_hash("./data/input_tmp.zip")

    
    print("answers_hash:", answers_hash)
    print("  input_hash:", input_hash)

    if answers_hash != answers_hash_old:
        print("New answers")
        decrypt("./data/answers", key)
        os.makedirs("./answers", exist_ok=True)
        shutil.unpack_archive("./data/answers_tmp.zip", "./answers", "zip")
        with open("./data/answers.hash" , 'w') as f:
            f.write(answers_hash) if answers_hash != None else f.write(answers_hash_old)

    if input_hash != input_hash_old:
        print("New inputs")
        decrypt("./data/input", key)
        os.makedirs("./input", exist_ok=True)
        shutil.unpack_archive("./data/input_tmp.zip", "./input", "zip")
        with open("./data/input.hash" , 'w') as f:
            f.write(input_hash) if input_hash != None else f.write(input_hash_old)

    

    os.remove("./data/answers_tmp.zip")
    os.remove("./data/input_tmp.zip")



if __name__ == "__main__":
    main()
