import re
import encoder

# Generates the output for a given word input in
# the form: word => equation = code
def readText(word):
    y = re.search("[a-z,A-Z]+", word)
    if (y is None) or (y.group() != word):
        return "Please only input text"
    else:
        eq = encoder.genEq(word)
        return word + " => " + eq + "= " + str(encoder.encode(word))

# Generates the output for a given code input in
# the form: code = equation => word
def readCode(code):
    y = re.search("[0-9]+", code)
    if (y is None) or (y.group() != code):
        return "Please input a Gödel number"
    else:
        word = ''.join(encoder.decode(int(code)))
        eq = encoder.genEq(word)
        return str(code) + " = " + eq + "=> " + word