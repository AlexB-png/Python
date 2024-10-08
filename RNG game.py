Rand=0
inpu=0
x=1
import random
rand=random.randint(1,100)

while rand != inpu:
    inpu=int(input("Pick a number between 1 - 100"))
    if rand==inpu:
        print("you win!")
        print("The random number was",rand)
        print("it took you",x,"tries")
    else:
        if inpu>rand:
            print("Too high")
            x=x+1
        else:
            print("Too low")
            x=x+1
    
