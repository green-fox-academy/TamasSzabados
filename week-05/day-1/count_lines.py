# Write a function that takes a filename as string,
# then returns the number of lines the file contains.
# It should return zero if it can't open the file, and
# should not raise any error.

def lines_number(filename = "my_file.txt"):
    try:
        f = open(filename, "r")
        length = len(f.readlines())
        f.close()
        return length
    
    except IOError:
        return 0

print(lines_number())