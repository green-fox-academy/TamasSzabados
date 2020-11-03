# Write function that joins the two lists by matching one girl with one boy in a new list
# If someone has no pair, he/she should be the element of the list too
# Exepected output: ["Eve", "Joe", "Ashley", "Fred"...]

girls = ["Eve", "Ashley", "Claire", "Kat", "Jane"]
boys = ["Joe", "Fred", "Tom", "Todd", "Neef", "Jeff"]

def making_matches(girls, boys):
    output = []
    if len(girls) > len(boys):
        for i in range(len(girls)):
            output.append(girls[i])
            output.append(boys[i])
    else:
        for i in range(len(boys)):
            if i < len(girls):
                output.append(girls[i])
            output.append(boys[i])  

    return output


print(making_matches(girls, boys))