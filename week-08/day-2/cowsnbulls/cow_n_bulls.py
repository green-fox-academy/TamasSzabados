import random

class Cow_n_bulls():
    def __init__(self):
        self.state = None
        self.numbers = []
        self.guesses = []
        self.counter = 0

    def random_numbers(self):
        for i in range(0,4):
            self.numbers.append(random.randint(0,9))
        return self.numbers
        print(self.numbers)

    def guess(self, number):
        if self.get_counter() < 3:
            self.guesses.append(number)
            self.counter += 1
            self.state = "playing"
        

        elif self.get_counter() == 3:
            self.guesses.append(number)
            self.counter += 1
            self.state = "finished"
        else:
            raise ValueError("No more numbers to guess, see the results")
        
        return self.counter

    def guess_results(self):
        if self.get_status() == "finished":
            list1 = []
            new_nums=[]
            new_guess=[]
            for i in range(len(self.numbers)):
                if self.numbers[i] == self.guesses[i]:
                    list1.append("Cow") 
                else:
                    new_nums.append(self.numbers[i])
                    new_guess.append(self.guesses[i])

            for i in range(len(new_guess)):
                if new_guess[i] in new_nums:
                    list1.append("Bull") 
            return ("You have: " + str(list1.count("Cow")) + " Cows and " + str(list1.count("Bull")) + " Bulls")
        
        elif self.get_status() == "playing":
            return ("you have to finish guessing 4 numbers")

    def reset(self):
        self.counter = 0
        self.state = None
        return self.counter

    def get_counter(self):
        return self.counter

    def get_status(self):
        return self.state


    

