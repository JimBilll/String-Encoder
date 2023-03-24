import encoder

# Define the word as an array of characters
word = ["A","B","H"]

# Encode and print the word
testcode = encoder.encode(word)

print("test code: " + str(testcode))

testword = encoder.decode(testcode)

print("eval test word: " + str(testword))