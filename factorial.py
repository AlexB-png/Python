
def factorial(n):
    
    if n==0:
        print("1")
    else:
        base=n
        while n!=1:
            
            base=base*(n-1)
            n-=1
        print(base)
n=int(input(""))
factorial(n)