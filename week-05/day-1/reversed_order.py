# Create a method that decrypts reversed-order.txt


import sys

def decrypt(file_name):
    try:
        with open(file_name,'r') as f:
            f = f.readlines()
            
        with open("reversed_back_order.txt",'w') as nf: 
            new_lines = []
            for line in reversed(f):
                new_lines.append(line)
            print(new_lines)    
            nf.writelines(new_lines)
            return True

    except IOError:
        print("Error occurred decrypting the file")
        sys.exit()
    
decrypt("reversed-order.txt")