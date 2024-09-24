#variables#
yes="false"
no="true"
year=0
x=0
year= input("What year is it")



#Defensive design#
 
for i in range(1,9999):
    i=str(i)
    if year==i:
        year=int(year)
        x=1

while x!=1:
    print("There was an incorrect input")
    year=input("Restart the programme")


#check if it's a leap year#

if year % 4 ==0: 
    #If divisible by 4 it is a leap year#    
    yes="true"
    no="false"

    if year % 100 == 0: 
        #However if you can divide by 100 then it is not a leap year#
        yes="false"
        no="true"

if year % 400 == 0: 
    #If it is divisible by 400 it is a leap year#
    yes="true"
    no ="false"



#returns whether its a leap year or not#

if yes == "true":
    print("It is a leap year")
elif no == "true":
    print("it is not a leap year")
else:
    print("Error")
    #Nothing should return an error#
