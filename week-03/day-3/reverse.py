# Create a function called 'reverse' which takes a string as a parameter
# The function reverses it and returns with the reversed string


def reverse(str):
    str1 = list(str)
    str1.reverse()
    str1 = ''.join(str1)
    return str1





toBeReversed = ".eslaf eb t'ndluow ecnetnes siht ,dehctiws erew eslaf dna eurt fo sgninaem eht fI"
print(reverse(toBeReversed))