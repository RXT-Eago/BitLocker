#

import random
import string
from passlib.hash import bcrypt


print(bcrypt.setting_kwds)
# ('salt', 'rounds', 'ident', 'truncate_error')
print(bcrypt.default_rounds)
# 12

hasher = bcrypt.using(rounds=13)  # Make it slower


password = input("Enter your unique password (keep it in head): ")
hashed_password = hasher.hash(password)
print("The key below is also important (copy paste it you will use later)\n")
print(str(hashed_password))
        
