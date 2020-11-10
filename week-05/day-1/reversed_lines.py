# Create a method that decrypts reversed-lines.txt
import sys

def decrypt(file_name):
    try:
        with open(file_name,'r') as f:
            f = f.readlines()
            
        with open("reversed_back_lines.txt",'w') as nf: 
            new_lines = []
            for line in f:
                line.rstrip()
                new_lines.append(line[::-1])
                
           
            print(new_lines)    
            nf.writelines(new_lines)
            return True

    except IOError:
        print("Error occurred decrypting the file")
        sys.exit()
    


decrypt("reversed-lines.txt")