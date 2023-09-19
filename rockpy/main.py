import random
user_wins=0
comp_wins=0

options = ["rock","paper","scissors"]

while True:
    user_input=input("choose rock,paper,scissors or q to QUIT: ").lower()

    if user_input == "q":
        break
    if user_input not in options:
        continue #re asks the question

    randon_num=random.randint(0,2)   
#rock 0","paper 1","scissors 2
    comp_pick = options[randon_num]
    print(f"computer picked {comp_pick}")

    if user_input == comp_pick:
        print("draw")
    elif user_input == "rock" and comp_pick == "scissors":
        print("you won")
        user_wins+=1
        
        
    elif user_input == "paper" and comp_pick == "rock":
        print("you won")
        user_wins+=1
       
    elif user_input == "scissors" and comp_pick == "paper":
        print("you won")
        user_wins+=1
    else:
        print("you lost !")
        comp_wins+=1
        
print("f you won {user_wins} times, computer won {comp_wins}")
print("goodbye")