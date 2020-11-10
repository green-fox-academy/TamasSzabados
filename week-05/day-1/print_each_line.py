  
# Write a program that opens a file called "my-file.txt", then prints
# each line from the file.
# If the program is unable to read the file (for example it does not exist),
# then it should print the following error message: "Unable to read file: my-file.txt"


file_name = "my_file.txt"

try:
    f = open(file_name, 'r')
    for line in f.readlines():
        line = line.rstrip()
        f.close()
        print(line)
except IOError:
    print('Unable to read file: ', file_name)
