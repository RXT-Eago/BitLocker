import time
import linecache
import json
import pyautogui
import traceback
import os
from sys import platform

from passlib.hash import bcrypt

import base64
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC

from cryptography.fernet import Fernet


hasher = bcrypt.using(rounds=13)  # Make it slower


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


def EncryptMessage(key, JSON):

    File_data = JSON    

    data = json.dumps(File_data)
    message = data.encode("utf-8")

    f = Fernet(key)
    encrypted = f.encrypt(message)
    #print(encrypted)

    with open('info.json', 'w') as json_file:
        json.dump(encrypted.decode("utf-8"), json_file, indent=4, separators=(',',': '))


def Decrypted(key):
    File_data = []
    with open('info.json') as File:
        File_data = json.load(File)

    data = json.dumps(File_data)
    message = data.encode("utf-8")

    f = Fernet(key)
    decrypted = f.decrypt(message)
    #print(decrypted)
    #print(decrypted.decode("utf-8") )
    res = json.loads(decrypted.decode("utf-8"))

    return res



def DisplayHelpCommand():
    print("\n - save [*WebSite*] [*Password*] #Save a new account for website\n")
    print(" - use [*WebSite*] #write the website's password directly where cursor is\n")
    print(" - rm [*WebSite*] #delete the WebSite and Password associated\n")
    print(" - list #List every website register\n")
    print(" - exit #close the programm\n")
    
def SaveCommand(WebSite, Password):

    #Save the password of associate website in secure file

    File_data = Decrypted(key)
    #print(File_data)
    #Password = Password.encode("utf-8")

    WebSiteInfo = {
        WebSite: Password,
    }

    #print(WebSiteInfo)
   
    File_data.update(WebSiteInfo)

    #print(File_data)

    EncryptMessage(key, File_data)


def UseWebSiteCommand(WebSite):
    
    #WebSiteFile = open('info.json', 'r')    
    WebSiteObject = Decrypted(key)

    if WebSite in list(WebSiteObject.keys()):
        print("\n*Place your cursor in the password field*")
        for i in range(5,0,-1):
            print(i)
            time.sleep(1)

        pyautogui.write(WebSiteObject[WebSite], interval = 0.2)

    else:
        print("WebSite unknown")
            
def RemoveWebSiteCommand(WebSite):
    WebSiteObject = Decrypted(key)

    try:
        del WebSiteObject[str(WebSite)]
    except Exception as E:
        print("Failed to remove the WebSite")

    EncryptMessage(key,  WebSiteObject)


def ListCommand():

    #WebSiteFile = open('info.json', 'r')    
    WebSiteObject = Decrypted(key)
    for WebSite in list(WebSiteObject.keys()):
        print(" - " + str(WebSite))
 


def Menu():
   

    #Once connect print the vailable command

    
    Args = input("/*: ")

    if Args.find("help") != -1:

        DisplayHelpCommand()

    elif Args.find("save") != -1:

        try:
            WebSite = Args.split()[1]
            NewPassWord = Args.split()[2]
            #print(str(WebSite) + " " + str(NewPassWord))

            #save parameter action
            SaveCommand(WebSite, NewPassWord)

        except Exception as E:
            print(E)
            #traceback.print_exc()
            print("Command not properly written")

    elif Args.find("use") != -1:

        try:

            WebSite = Args.split()[1]
            #print(str(WebSite))

            #use parameter action
            UseWebSiteCommand(str(WebSite))

        except Exception as E:

            print("Command not properly written")

    elif Args.find("rm") != -1:

        try:

            WebSite = Args.split()[1]
            #print(str(WebSite))

            #use parameter action
            RemoveWebSiteCommand(str(WebSite))

        except Exception as E:

            print("Command not properly written")

    elif Args.find("list") != -1:

        ListCommand()

    elif Args.find("exit") != -1:

        exit()

    else:
        print("Command unvailable or inexsitant")

    #print(Agrs)

def Connection():

    global PASSWORD
    PASSWORD = input("enter your app password: ")
    CorrectLine = input("select the correct line: ")

    #f = open("password.txt", "r")
    hash = linecache.getline('password.txt', int(int(CorrectLine)))
    hash = hash[:-1]
    
    return hasher.verify(str(PASSWORD), str(hash))

def ClearConsole():
    if platform == "linux" or platform == "linux2":
        os.system('clear')
    elif platform == "win32" or platform == "win64":
        os.system('cls')
        
while True:
    if Connection():
        ClearConsole()
        print("try *help* to display available command")
        global key
        key = GetKeyFromPassword()
        while(1):
            Menu()
    else:
        "Wrong Password"
