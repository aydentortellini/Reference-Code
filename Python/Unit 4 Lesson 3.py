"""def greetings():
    print("Hi there")
    print("nice to meet you")


for i in range(3):
    greetings()"""



'''def print_value(x):
    print(x)

y = 5

print_value("dog")
print_value(y)
print_value(6)'''




'''def add_two(x):
    return x+2



new_variable = add_two(5)
print(new_variable)'''


import random
def check_guess(guess, number):
    return guess == number

def guess_game():
    number = random.randint(1,10)
    for i in range(5):
        if check_guess(int(input("guess: ")), number):
            print("Correct!");
            return "out of attempts! The number was " + str(number)
        else:
            print("try again")


print(guess_game())


