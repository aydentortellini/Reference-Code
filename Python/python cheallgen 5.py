#1
rhyme = input("Type in the first line of a nursery rhyme: ")
print(len(rhyme))

#2
name = input("Enter your first name: ")
len(name)
if len(name) > 5:
    print(name.lower())
if len(name) < 5:
    name2 = input("Enter surname: ")
    print(name + name2)
if len(name) == 5:
    print(name)

#3
print("1(Square " "2(Triangle")
Area = int(input("Enter 1 or 2: "))

if Area == 1:
    sqaure = int(input("What is one of the side lengths?: "))
    answer1 = (sqaure * 4)
    print("The area is" , answer1)
if Area == 2:
   triangle1 = int(input("What is the base length?: "))
   triangle2 = int(input("What is the height?: "))
   answer2 = (triangle1 * triangle2 / 2)
   print(answer2)
if Area > 2:
    print("error")

#4
import random
print(" Red, Blue, Green, Purple, Black")
color1 = input("Enter a color from above: ")
color2 = random.choice(["red","blue","green","purple","black"])
print(color2)
if color1.lower() == color2.lower():
    print("Well done")
