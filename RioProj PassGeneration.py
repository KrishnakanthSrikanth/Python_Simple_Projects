#Help Rio to generate random password--By LetsUpgrade

import string
import random


def passwordCreation():
    stringLength = 10
    passwordType = string.ascii_letters + string.digits + string.punctuation
    password = random.sample(passwordType, stringLength)
    return ''.join(password)


print(passwordCreation())

# Logic: random.sample() is used to generate values without repetition and as per the input passed to it. Also,
# string module has various in built methods by which I have used lowercase and uppercase letters(string.ascii_letters),
# for digits (string.digits) and for symbols(string.punctuation). With these i have generated a random password of length 10.
