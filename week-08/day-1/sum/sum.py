def sum1(args):
    sum1 = 0
    if args == None or args == []:
        raise ValueError("No arguments")
    for i in args:
        sum1 += i
    
    return sum1

