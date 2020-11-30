def count_letters(str1):
    if type(str1) != str:
        raise TypeError("You must provide a string")
    else:
        dict1= dict()
        for i in str1:
            dict1[i]= str1.count(i)

        return dict1
        

