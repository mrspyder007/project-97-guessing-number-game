import random
num=random.randint(1,9)
chances=0
print("Guess a no. between 1 and 9")

while(chances<5):
    guess=int(input("Enter no:"))
    if(guess==num):
        print("You won")
        break
    elif(guess<num):
          print("Your guess was too low: Guess a number higher than", guess)
    else:
          print("Your guess was too high: Guess a number lower than", guess)
    chances=chances+1

if not chances<5:
    print("You Loose")



