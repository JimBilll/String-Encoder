# Gödel Word Encoder

### *By James McLean*

This program can be run in two operation modes; encode and decode. You will be encouraged to select a mode upon running.

- Encode - Enter a word and it will be encoded to a Gödel number.
- Decode - Enter a Gödel number and it will be decoded to a word

At present, the program lacks input validation, so will crash if anything other than alphabetical text is used. (Also if the word is too long it'll crash because Gödel numbers can easily get too big for Python to deal with).