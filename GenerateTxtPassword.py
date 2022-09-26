#This code will generate multiple hash to confuse an eventual breach security

# We need to create thousand of this kind od password looklike but only the operator know the associate
# line

# $2b$13$H9.qdcodBFCYOWDVMrjx/uT.fbKzYloMYD7Hj2ItDmEOnX5lw.BX.
# \__/\/ \____________________/\_____________________________/
# Alg Rounds  Salt (22 char)            Hash (31 char)

import random
import string
from passlib.hash import bcrypt
from getpass import getpass

print(bcrypt.setting_kwds)
# ('salt', 'rounds', 'ident', 'truncate_error')
print(bcrypt.default_rounds)
# 12

hasher = bcrypt.using(rounds=13)  # Make it slower

#Aleatoire lettre
def MotAlea():
    Mot = ""
    for i in range(8):
        Mot += str(random.choice(string.ascii_letters))
        Mot += str(random.choice(string.punctuation))
    
    return Mot

with open('password.txt', 'w') as f:
    for i in range(500):
        password = MotAlea()
        hashed_password = hasher.hash(password)
        f.write(str(hashed_password) + "\n")
