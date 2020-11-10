# Create a method that decrypts the duplicated-chars.txt
import sys

def decrypt(file_name):
    try:
        with open(file_name,'r') as f:
            f = f.read()
        with open("simple-chars.txt",'w') as nf:
            
            new_lines = ""
            for char in range(len(f)):
                if char% 2!= 0:
                    new_lines += f[char]
            nf.write(new_lines)
        return True
         

    except IOError:
        print("Error occurred decrypting the file")
        sys.exit()


decrypt("duplicated-chars.txt")