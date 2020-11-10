# Write a function that copies the contents of a file into another
# It should take the filenames as parameters
# It should return a boolean that shows if the copy was successful

def copy_file(filename, new_filename):
    try:
        with open(filename,'r') as f:
            f = f.readlines()
        with open(new_filename,'w') as nf:
            for lines in f:
                nf.write(lines)
        return True

    except IOError:
        print("Error occurred while copying the file")




print(copy_file("my-file.txt", "new_file.txt"))