# importing the modules
import random
import string

chars = " " + string.punctuation + string.digits + string.ascii_letters
chars = list(chars)# Converting it into a list
key = chars.copy()# we made a clone of chars and assigned it to key

random.shuffle(key)# randomly shuffles key
print(f"chars : {chars}")
print(f"key : {key}")

plain_text = input("Enter a message to encrypt: ")
encrypted_message = ""

for letter in plain_text:
    index = chars.index(letter) #check the index of every letter of input
    encrypted_message += key[index] #substitutes every letter in input with every letter in key of same index
print(f"Original text : {plain_text}")
print(f"Encrypted text : {encrypted_message}")
