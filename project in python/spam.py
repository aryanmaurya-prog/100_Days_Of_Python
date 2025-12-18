import random 
number = random.randint(1,100)
guess = int(input("Guess a number between 1 and 100:\n"))
while guess != number:
    if guess > number:
        print("Too High!")
    else:
        print("Too low!")
        
    guess = int(input("Try Again: "))
print("Congratulations you guessed it!")