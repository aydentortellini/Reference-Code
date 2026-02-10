
num1 = int(input("Enter a number: "))
num2 = 10

if num1 > 10:
    print("this is over 10")
elif num2 == 10:
    print("this is equal to 10")
else:
    print("this is under 10")

#This code asks for age and returns category

age = int(input("Enter your age: "))

if age <0:
    print("Age cant be negitive")
elif age < 18:
    print("you are a minor")
elif age <65:
    print("you are an adult")
else:
    print("you are a senior citizen")


"""
== Equal to
!= Not equal to
> Greater than
< Less then
>= Greater than or equal to
<= Less than or equal to

Logical Operators
and - Both conditions must be met
or - Ether condition musts be met
"""

num1 = 8


if num1 < 5 and num1 !=3:
    print("the number is not 3")
elif num1 == 4 or num1 ==8:
    print("Then number is 4 or 8")
