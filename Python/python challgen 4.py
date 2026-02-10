#1
num3 = int(input("Enter a number under 20: "))

if num3 <= 20:
    print("thank you")
if num3 >= 20:
    print("to high")

#2
color = input("Whats your favrite color?: ")

if color.lower() == "red":
    print("me to!")
else:
    print("i dont like" ,color, "i prefer red")

#3

age = int(input("how old are you?: "))

if age >= 18:
    print("you can vote")
elif age == 17:
    print("you can learn to drive")
elif age == 16:
    print("you can learn to drive")
else:
    print("you can trick or treat")

#4
num1 = int(input("enter 1,2 or 3: "))

if num1 == 1:
    print("thank you")
elif num1 == 2:
    print("well done")
elif num1 == 3:
    print("correct")
else:
    print("ERROR")
