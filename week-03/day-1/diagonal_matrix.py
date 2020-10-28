# - Create (dynamically) a two dimensional list
#   with the following matrix. Use a loop!
#
#   1 0 0 0
#   0 1 0 0
#   0 0 1 0
#   0 0 0 1
#
# - Print this two dimensional list to the output

matrix = []
for i in range(4):
    sub_matrix =[]
    for k in range(4):
        if k == i:
            x = 1
        else:
            x = 0    
        sub_matrix.append(x)
    matrix.append(sub_matrix)
    
    
print(matrix)
