import encoder

def encodeMode():
    inputWord = input("Enter a word to encode: ")
    # Define the word as an array of characters
    word = list(inputWord)
    # Encode and print the word
    code = encoder.encode(word)
    print("Encoded word: " + str(code))


def decodeMode():
    inputCode = int(input("Enter a code to decode: "))
    word = encoder.decode(inputCode)
    print("Decoded word: " + "".join(word))

inputMode = input("Gödel Word Encoder\nEnter mode - Encode (e), Decode (d), Exit (x): ")

if inputMode == "e":
    encodeMode()
elif inputMode == "d":
    decodeMode()
elif inputMode == "x":
    print("Exiting.")