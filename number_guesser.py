import random

print("Welcome to Number Guesser Game! ")
end=int(input("Enter the upper bound: "))

rand_no=random.randint(0,end)
guess=-1
tries=0
while guess!= rand_no :
    print("\nGuess a number between 0 and", end, ":")
    guess = int(input())
    if (guess < rand_no):
        print ("Too low!")
        tries+=1
    elif (guess > rand_no):
        print ("Too high!")
        tries+=1
    else:
        print ("Congratulations!! You guessed it right.")
        break
print("You got it in",tries, "tries! :3")


