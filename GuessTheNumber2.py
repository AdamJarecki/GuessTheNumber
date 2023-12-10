#This is a second attempt, ideally one that I will do without much auto complete.

import random as r

class GuessTheNumber:
    def __init__(self):
        self.number = r.randint(1,20)
        self.tries = 0
        self.win = False
        self.guess = 0
    
    def guessTheNumber(self):
        while self.tries < 6 and self.win == False:
            print("Welcome, mortal! \nGuess a number from 1 to 20!")
            guess = int(input("Guess: "))
            if guess == self.number:
                print("You got it!")
                self.win = True
            elif guess > self.number:
                print("Not quite, your guess was too high!")
            else:
                print("Not quite, your guess was too low!")
            self.tries += 1 
        print("You lose! The number was " + str(self.number) + "!")


game = GuessTheNumber()
game.guessTheNumber()