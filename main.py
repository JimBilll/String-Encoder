import encoder

# Define the word as an array of characters
word = ["A","B","H"]

# Encode and print the word
testcode = encoder.encode(word)

print("test code: " + str(testcode))

testfactor = encoder.decode(testcode)

print("test factor: " + str(testfactor))

print("eval test factor: " + str(encoder.evalFactors(testfactor)))