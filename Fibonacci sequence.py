x=0
y=1
z=0
value=int(input("Input a number as a limit"))
for i in range(100000000000):
    if y > value:
        break
    else:
        z=x+y
        if z > value:
            break
        else:
            print(z)
            x=y+z
            if x > value:
                break
            else:
                print(x)
                y=z+x
                if y > value:
                    break
                else:
                    print(y)