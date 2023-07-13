import random

comp_win=0
user_win=0
list=["rock","paper","scissors"]

while True:
    user=input("Enter rock/paper/scissors or quit: ")
    if user.lower()=='quit':
        break
    if user.lower() not in list:
        continue

    comp=random.randint(0,2)
    print("\nComputer picked",list[comp],"!")

    if user.lower()==list[comp]:
        print("Both picked same! ")
    elif user.lower()=="rock" and list[comp]=="scissors":
        print("You won!")
        user_win+=1
    elif user.lower()=="scissors" and list[comp]=="paper":
        print("You won!")
        user_win+=1
    elif user.lower()=="paper" and list[comp]=="rock":
        print("You won!")
        user_win+=1
    else:
        print("Sorry! You lost.")
        comp_win += 1

print("You won "+str(user_win)+" out of "+str((user_win+comp_win))+" times!")
print("Thanks for playing! :3")
