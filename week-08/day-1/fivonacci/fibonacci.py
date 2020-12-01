def fibonacci(index):
    if type(index) != int:
        raise TypeError("index must be a whole number")
    else:
        a = 0
        b = 1
        for i in range(0, index):
            temp = a
            a = b
            b = temp + b
    return a
