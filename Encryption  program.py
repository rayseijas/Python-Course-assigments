import random
import string

chars = string.ascii_letters + string.digits + string.punctuation + " "
chars = list(chars)

key = chars.copy()
random.shuffle(key)



Text= input("Enter your text")
chyperText = ""

for letter  in Text:
    index = chars.index(letter)
    chyperText  += key[index]


print(f" texto encriptado {chyperText}")
print(f" texto decriptado {Text}")


