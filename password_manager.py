
def add():
    username=input("Username: ")
    pwd=input("Password: ")

    with open("passwords.txt","a") as f:
        f.write(username+"|"+pwd+"\n")

def view():
    with open("passwords.txt","r") as f:
        for line in f.readlines():
            data=line.rstrip()
            username,pwd=data.split("|")
            print("Username: "+username+", Password: "+pwd)


while True:
    option=input(" Would you like to add an account or view all passwords? (add/view) Press q to quit: ").lower()
    if option=="q":
        break

    if option=="add":
        add()
    elif option=="view":
        view()
    else:
        print("Invalid choice ")
        continue
