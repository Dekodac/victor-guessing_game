import random

class GuessingGame():
    def __init__(self, answer):
        self.answer = answer
        self.userSolved = False
        self.guessesArr = []

    def guess(self, user_guess):
        self.guessesArr.append(user_guess) 
        if user_guess == self.answer:
            self.userSolved = True
            print("You got it!")
            print(f'These were your guesses: {self.guessesArr}')
        elif user_guess > self.answer:
            print("Too High!")
        elif user_guess < self.answer:
            print("Too low!")

    def solved(self):
        return self.userSolved

def main():
    game = GuessingGame(random.randint(1, 20))
    print("Welcome to my guessing game!")

    while not game.solved():
        try:
            last_guess = int(input("Enter your guess: "))
            game.guess(last_guess)
        except ValueError:
            print("Please enter a valid number!")

if __name__ == "__main__":
    main()
