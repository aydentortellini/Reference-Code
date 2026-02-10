
#1
total = 0
for i in range(5):
    number = int(input("Enter number: "))
    inclued = input("Do you want this in the total: ")
    if inclued.lower() == "yes":
        total = total + number
print("the total is", total)

#2

people = int(input("How many people do you want to invite?: "))

if people <= 10:
    for i in range(people):
        name = input("what is the name of the people you want (one at a time): ")
        print(name, "has been invited")
if people > 10:
    print("to many people")

#3
total = 0
while total < 50:
    num = int(input("enter a number: "))
    total = total + num

print("The total is", total)


#4
countpeople = 1
while True:
    name1 = input("Enter the name of the person you want to invite: ")
    print(name1, "Has been invited")
    countpeople = countpeople + 1
    invitemore = input("Do you want to invite more? (yes/no): ")
    if invitemore.lower() == "no":
        break
print("You have invited", countpeople ,"people")

#5
compnum = 50
count = 0
guess = int
while guess != compnum:
    guess = int(input("Guess a number: "))
    if guess > compnum:
     count = count + 1
     print("too high")
     
    if guess < compnum:
     count = count + 1
     print("too low")

if guess == compnum:
    print("Well done it took you", count ,"tries")


