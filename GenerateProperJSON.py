import base64
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC


def GetKeyFromPassword():
    password_provided = PASSWORD  # This is input in the form of a string
    password = password_provided.encode()  # Convert to type bytes
    salt = b'salt_'  # CHANGE THIS - recommend using a key from os.urandom(16), must be of type bytes
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=100000,
        backend=default_backend()
    )
    key = base64.urlsafe_b64encode(kdf.derive(password))  # Can only use kdf once
    return key

from cryptography.fernet import Fernet
import json

def EncryptMessage(key, JSON):

    File_data = JSON    

    data = json.dumps(File_data)
    message = data.encode("utf-8")

    f = Fernet(key)
    encrypted = f.encrypt(message)
    print(encrypted)

    with open('info.json', 'w') as json_file:
        json.dump(encrypted.decode("utf-8"), json_file, indent=4, separators=(',',': '))


def main():
    global PASSWORD
    PASSWORD = input("Enter your unique password: ")
    key = GetKeyFromPassword()

    WebSiteInfo = {}# On initialise le tout premier format JSON avec une nouvelle clé
    EncryptMessage(key, WebSiteInfo)


main()
