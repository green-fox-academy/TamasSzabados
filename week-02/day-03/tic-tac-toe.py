def tic_tac_toe():
    player1 = "X"
    player2 = "O"
    first_player = True
    coordinates = [[" "," "," "],[" "," "," "],[" "," "," "]]
    def display(coordinates):
        for i in range(len(coordinates)):
            for j in range(len(coordinates[i])):
                print("|" + coordinates[i][j] + "_", end=" " )
            print()

    game_on = True

    while game_on == True:
        if coordinates[0][0] and coordinates[1][0] and coordinates[2][0] == "X":
            print("Player one wins!")
            display(coordinates)
            game_on = False
        elif coordinates[0][0] and coordinates[1][0] and coordinates[2][0] == "O":
            print("Player two wins!")
            display(coordinates)
            game_on = False
        elif not all((x, " ") for x in coordinates):
            print("It is draw!")
            display(coordinates)
            game_on = False

        else:
            
        #the check should be extended with more game situations, and if all slot is full

            if first_player == True: 
                x = int(input("First player! Please enter the first coordinate: "))
                if x < 1 or  x > 3 :
                    raise Exception("wrong coordinates")
                y = int(input("First player! Please enter the second coordinate: "))
                if y < 1 or  y > 3 :
                    raise Exception("wrong coordinates")
                if coordinates[x-1][y-1] != " ":
                    raise Exception("not empty slot")
                else:    
                    coordinates[x-1][y-1] = player1
                
                display(coordinates)
                first_player = False

            else: 
                x = int(input("Second player! Please enter the first coordinate: "))
                if x < 1 or  x > 3 :
                    raise Exception("wrong coordinates")
                y = int(input("Second player! Please enter the second coordinate: "))
                if y < 1 or  y > 3 :
                    raise Exception("wrong coordinates")

                if coordinates[x-1][y-1] != " ":
                    raise Exception("not empty slot")
                else:    
                    coordinates[x-1][y-1] = player2
                display(coordinates)
                first_player = True

    return coordinates

tic_tac_toe()