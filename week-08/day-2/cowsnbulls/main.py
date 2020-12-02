from cow_n_bulls import Cow_n_bulls

def main():
    player = Cow_n_bulls()
    i = 0 
    print(" To play cow 'n' bulls please enter a number 4 times!")
    while i < 4:
        user_input = int(input("Please enter a number between 0 an 9:  "))
        player.guess(user_input)
        i +=1

    print(player.random_numbers())
    print(player.guess_results())


if __name__ == '__main__':
    main()