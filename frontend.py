import re
import encoder

def readText(x):
    y = re.search("[a-z,A-Z]+", x)
    if (y.group() != x):
        print("unrecognised characters")
    else:
        print(x)
        print(y)
        print(encoder.encode(x))

def readCode(x):
    y = re.search("[0-9]+", x)
    if (y.group() != x):
        print("unrecognised characters")
    else:
        print(x)
        print(y)
        
        word = ''.join(encoder.decode(int(x)))
        print(word)