#1
num1 = int(input("Enter a number: "))
num2 = int(input("Enter a diffrent number: "))

if num1 >= num2:
    print(num1,",",num2,)
else:
    print(num2,",",num1,)

#2
num3 = int(input("Enter a number between 10-20: "))

if num3 >= 10 and num3 <= 20:
    print("thank you")
else:
    print("wrong")
#3
rain = input("is it raining? (yes) (no): ")
wind = input("is it windy (yes) (no): ")
if rain.lower() == "yes":
    if wind.lower() == "yes":
        print("its to winded for an unbrella")
if wind.lower() == "no" and rain.lower() == "yes":
    print("take an unbrella")
else:
    print("enjoy your day")

#4

num4 = int(input("Enter a number: "))

if num4 >= 10 and num4 <= 20:
    print("Correct")
if num4 >= 20:
    print("too high")
if num4 <= 10:
    print("too low")
