from os import *
from sys import *
from collections import *
from math import *

def isArmstrong(num):
    original = num

    # Extract no. of digits
    count = 0
    temp = num

    while temp > 0:
        count += 1
        temp //= 10

    # Extract digit by digit and armstrong calc
    total = 0
    temp = num

    while temp > 0:
        digit = temp % 10
        total = total + (digit ** count)
        temp //= 10

    return total == original