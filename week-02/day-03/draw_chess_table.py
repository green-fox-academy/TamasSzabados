# Crate a program that draws a chess table like this
#
# % % % % 
#  % % % %
# % % % %
#  % % % %
# % % % %
#  % % % %
# % % % % 
#  % % % %
#

for i in range(8):
    if i % 2 ==0:
        print("% "*4)
    else:
        print(" %"*4)