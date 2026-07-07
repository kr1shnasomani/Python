from math import *
from collections import *
from sys import *
from os import *

## Read input as specified in the question.
## Print output as specified in the question.
x = int(input())
y = int(input())

while y != 0:
    remainder = x % y
    x = y
    y = remainder

print(x)