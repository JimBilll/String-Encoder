import re

def readInp(x):
    y = re.search("[a-z,A-Z]+", x)
    if (y.group() != x):
        print("unrecognised characters")
    else:
        print(x)
        print(y)