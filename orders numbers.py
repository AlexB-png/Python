import random
numbers = random.sample(range(1000, 10000), 100) #using sample will return an index that can later be read from in order to order the list#
numbers.sort() #this will sort the numbers from largest to smallest#
print(numbers)
x=0
x=len(numbers) #figures out how many numbers are in the list#
print("") #Leaves a space between the list#
print(numbers[x-1],"is the largest number in the list") #returns the largest number#
average=0
total=0
for i in numbers:
    total = total + i
total= total/len(numbers)
print("")
print(total,"is the average")

