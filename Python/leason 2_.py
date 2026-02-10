'''

num = int(input("give me a number"))

if num >= 10:
    if num <= 20:
        print("between 10 and 20")
    else:
        print("this is over 20")
else:
    print("under ten")
'''
'''

word = input("type monkey or dog: ")

if word.lower() == "monkey": 
    print("the word is monkey")
elif word.upper() == "Dog":
    print("the word is dog")
else:
    print("the word is not monkey")
'''

user_input = str(input("enter the word 'Python': "))

if user_input.lower() == "python":
    print("you entered the right word")
elif user_input == "":
    print("you didnt put anything")
else:
    print("you didnt enter the right word")
