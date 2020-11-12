def greatest_comm_div(num1, num2):
    if(num2==0): 
        return num1 
    else: 
        return greatest_comm_div(num2,num1%num2) 


print(greatest_comm_div(60,48))