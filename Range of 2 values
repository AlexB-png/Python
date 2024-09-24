quit=0
while quit != "yes":

    #variables
    x=0
    a=0
    b=0
    y=0

    #inputs
    print("The minimum value is 0 / The maximum is 9999")
    a=input("First number")
    b=input("Second number")

    #defensive design A
    for i in range(9999999):
        i=str(i)
        if i==a:
            x=1
    if x != 1:
        print("Error")
    else:
        a=int(a)

    #defensive design B
    for i in range(9999999):
        i=str(i)
        if i==b:
            y=1
    if y != 1:
        print("Error")
        print("please input a low number then a high number")        
    else:
        b=int(b)


    #Check that B is higher than A
    if x==1 and y==1:
        if a > b:
            print("please input a low number then a high number")
        else:
        #print all the values from A to B
            if x==1:
                for i in range(a,b+1):
                    print(i)
    quit=input("type yes to quit")
