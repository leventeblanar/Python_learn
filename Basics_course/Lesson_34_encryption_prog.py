import random  # to have shuffle to use - mix a list of characters
import string # instead of declaring several characters separately, we are calling them using the string module

chars = " " + string.punctuation + string.digits + string.ascii_letters

chars = list(chars)   # reassigning chars as a list
key = chars.copy() # key is the relative list that changes every time an input is pushed - relative to the chars list it defines what the characters will be replaced to based on the character index

random.shuffle(key) 

print(f"chars: {chars}")
print(f"key: {key}")

### ENCRYPT ###

plain_text = input("Enter a message to encrypt: ")
cipher_text = ""  # the name of the encrypted message - assigning an empty string to be able to replace it to the encrypted message

for letter in plain_text:
    index = chars.index(letter)
    cipher_text += key[index]

print(f"original message: {plain_text}")
print(f"encrypted mesage: {cipher_text}")

### DECRYPT ###

cipher_text = input("Enter a message to decrypt: ")
plain_text = ""  # the name of the encrypted message - assigning an empty string to be able to replace it to the encrypted message

for letter in cipher_text:
    index = key.index(letter)
    plain_text += chars[index]

print(f"original message: {cipher_text}")
print(f"encrypted mesage: {plain_text}")
