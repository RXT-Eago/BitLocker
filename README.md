# BitLocker
Gestionnaire de mot de passe sécurisé

# Introdution

This projet has been created for personnal everyday usage, I will try to explain simply how it work and detail every fonctionnality available at the moment

# First Step

You will need to install all necessary python package using pip module:

> pip install -r requirements.txt

1. **Generate your own secure key**

    To use the App you will need a unique password that you will never forget, it will give you full access of the BitLocker. For that, you will need to lauch this command from the command prompt:

    > python GenerateUniquePassword.py

    Then enter your password (don't forget to keep it in your mind).
Normally after you type your password a key with this format will appear **you must save this key (copy paste it somewhere we will use it after**)

2. **Generate multiple fake key (optional)**
   
    Once you have generated a hashed key from your unique password you need to store it in a file. ***(You can skeep this part this is optional but fun)***

    Run this command:

    > python GenerateTxtPassword.py

    This command will create 500 random hashed key in the password.txt file. This is just to create confusion in case someone would try to brut attack it (as I say it's optional)
Once the program ended you can copy paste your unique key generated before into the password.txt file wherever you want (The line of your choice perhaps ***you will need to remember the line number***)

1. **Generate a secure JSON file to store your passwords**
   
   Once you have created your unique hashed key and store it into the password.txt you will need to create a JSON file to store the your future password data.
   This JSON file will be created using the same 'admin' password that you use previously (the one that you should keep in mind).
   This programme is going to initialise the .json file with you own hashed key so that no one can open the file and see your password llike that.

   > python GenerateProperJSON.py

   Once done if you open your .json file you will see hashed data unreadable.

2. **Start the App**   
It's now the moment to use the app after all the prerequires.

    To start the app run this command:

    > python main.py

    you will have to enter you 'admin' password and the correct line correspondance of your hashed key in the password.txt file.

    ![Menu of the app](/doc/images/App_Menu.png)

    This is how the menu will appear. You can use and test all the command.



