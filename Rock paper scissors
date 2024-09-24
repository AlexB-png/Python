import random
answer=0
choice=0
computer=0
compscore=0
score=0
print("The computer will choose")
print("r=rock p=paper s=scissors")
print()
while score < 5 and compscore < 5:
    choice=input("What do you choose?")
    computer=random.randint(1,3)
    if computer==1 and choice=="r":
        print("Its a draw")
    elif computer==2 and choice=="r":
        print("Computer wins")
        compscore=compscore+1
    elif computer==3 and choice=="r":
        print("You win")
        score=score+1

    elif computer==1 and choice=="p":
        print("you win")
        score=score+1
    elif computer==2 and choice=="p":
        print("Its a draw")
    elif computer==3 and choice=="p":
        print("Computer Wins")
        compscore=compscore+1

    elif computer==1 and choice=="s":
        print("Computer Wins")
        compscore=compscore+1
    elif computer==2 and choice=="s":
        print("You Win")
        score=score+1
    elif computer==3 and choice=="s":
        print("Its a draw")
    else:
        print("Invalid")
        score=0
    if computer==1:
        print("the computer chose rock")
    elif computer==2:
        print("the computer chose paper")
    elif computer==3:
        print("the computer chose scissors")
    score=int(score)
    compscore=int(compscore)
    print("The score is",score,"-",compscore)
    
if score == 5:
    print("\033[0;37;40mYou Win\n")
elif compscore == 5:
    print("\033[0;37;40mComputer wins\n")
else:
    print("Error")
    
