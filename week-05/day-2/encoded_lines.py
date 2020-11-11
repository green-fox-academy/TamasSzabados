# Create a method that decrypts encoded-lines.txt

import sys

def decrypt(file_name):
    new_text = ""
    try:
        with open(file_name,'r') as f:
            f = f.read() 
            for char in f:
                if char != " " and char !="\n":
                    new_text += chr(ord(char) - 1)
                else:
                    new_text += char
    except IOError:
        print("Error occurred decrypting the file")
        sys.exit()
    print(new_text)

decrypt("encoded-lines.txt")