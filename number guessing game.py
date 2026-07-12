import random
print("Welcome to the number guessing game 👾🤖 ")
numb_of_guess=random.randint(1,100)
attempts=0
while True:
    guess=int(input("enter a number betweeen 1 to 100:"))
    attempts+=1
    if guess<numb_of_guess:
        print("you are too low 🤷‍♀️")
    elif guess > numb_of_guess:
        print("you are too high 😒")
    else:
        print(f"yahh ! you got correct in {attempts} attempts🥳⭐🎉 ")