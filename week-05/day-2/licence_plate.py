
import re
import sys

def licence_finder(file_name = "words.txt"):
    while True:
        user_input = input("Please enter your licence plate number: ")
        if re.match("^[a-zA-Z]{3}[- ]?[0-9]{3}", user_input) is not None: 
            break
        else:
            raise Exception("Not a valid licence number")
    words_list=[]
    try:
        with open(file_name, 'r', encoding='utf8') as f:
            f = f.readlines() 
            for line in f:
               
                if line.find(user_input[0:3].lower()) != -1:
                    words_list.append(line)

            

    except IOError:
        print("Error occurred decrypting the file")
        sys.exit()
    word_string = ' '.join(map(str, words_list))
    if len(words_list) == 0:
        print("Sorry! Did not find any word to help you to remember.")
    else:
        print(word_string)
licence_finder()
