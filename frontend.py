import re
import encoder

def readText(x):
    y = re.search("[a-z,A-Z]+", x)
    if (y is None) or (y.group() != x):
        return "Please only input text"
    else:
        return encoder.encode(x)

def readCode(x):
    y = re.search("[0-9]+", x)
    if (y is None) or (y.group() != x):
        return "Please input a Gödel number"
    else:
        word = ''.join(encoder.decode(int(x)))
        return word