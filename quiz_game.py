print("Welcome to Naruto Quiz Game! ")
answer=input("Do you wish to play? ")
if answer.lower()=="yes":
    print("\nLet's start the quiz!")
    score=0

    #q1
    answer=input("What is the name of the Sannin known as the 'Legendary Sucker'? ")
    if answer.lower()=="jiraiya":
        print("Correct! ")
        score+=1
    else:
        print("Incorrect! It's Jiraiya")

    #q2
    answer=input("Which character has the ability to control sand? ")
    if answer.lower()=="gaara":
        print("Correct! ")
        score+=1
    else:
        print("Incorrect! It's Gaara")

    #q3
    answer=input("What is the name of the ninja group led by Hidan and Kakuzu? ")
    if answer.lower()=="the immortal duo" or answer.lower()=="the zombie combo":
        print("Correct! ")
        score+=1
    else:
        print("Incorrect! It's  The Immortal Duo (or the 'Zombie Combo')")

    #q4
    answer=input("Which character is the jinchuriki of the Two-Tailed Beast? ")
    if answer.lower()=="yugito nii":
        print("Correct! ")
        score+=1
    else:
        print("Incorrect! It's Yugito Nii")

    #q5
    answer=input("Who is Naruto's mother? ")
    if answer.lower()=="kushina uzumaki":
        print("Correct! ")
        score+=1
    else:
        print("Incorrect! It's Kushina Uzumaki")

    print("You scored "+str(score)+" out of 5, ie. "+str((score*100/5)))
    print("Thanks for playing! :3")
else:
    print("That's too bad, maybe next time! :3")



    