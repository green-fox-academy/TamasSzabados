# Create a function that takes 3 parameters: a path, a word and a number
# and is able to write into a file.
# The path parameter should be a string that describes the location of the file you wish to modify
# The word parameter should also be a string that will be written to the file as individual lines
# The number parameter should describe how many lines the file should have.
# If the word is "apple" and the number is 5, it should write 5 lines
# into the file and each line should read "apple"
# The function should not raise any errors if it could not write the file.


import os.path


def write_file(path, word, number):
    try:
        with open(os.path.join(path, "my-file.txt"), 'w') as f:
            for i in range(number):
                f.write(word + "\n")

    except IOError:
        print("")
path1 = 'c:/Users/tamas/Documents/IBS/codingFundamentals/greenfox/tszabad/week-05/day-1'
write_file(path1, "Apple",5)