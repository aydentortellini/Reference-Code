import random
import math
player_name = input("Whats your name?: ")
print("Hello" ,player_name,)
food = 0
adventure = input("Do you want to go on an adventure?: ")
again = "yes"

if adventure.lower() == "yes":
    print("TELEPORTING")
    quest1 = input("You are now in the jungle do you want to go look for food?: ")
    if quest1.lower() == "yes":
       animal = random.choice(["Deer","Duck","Turkey"])
       print("you find a",animal,)
       kill = input("Do you want to kill it?: ")
    if kill.lower() == "yes":
        shot_hit = random.choice([True,False])
        if shot_hit == True:
            print("You got him")
            food = food + 20
            print("you have", food ,"food")
        while again.lower() == "yes":
            if shot_hit == False:
                shot_hit = random.choice([True,False])
                print("You missed")
                again = input("Do you want to try again?: ")

            elif shot_hit == True:
                print("You got him")
                food = food + 20
                print("you have", food ,"food")
                break
            if again.lower() == "yes":
                continue
            elif again.lower() == "no":
                print("you move on to explore")
                break


    print("you find a group of scientist in a camp")
    print("they say they will take you home but only three of them can go")
    scientist = input("do you want to leave with them?: ")
    if scientist.lower() == "yes":
        print("there is Jacob, Jake, Alvin, Calvin, Nicholas")
        choose = input("choose your pilot first (i recomend calvin): ")
        if choose.lower() == "calvin":
            print("great choice")
        else:
            print("cool")
        choose1 = input("choose another person: ")
        if choose1.lower() == "nicholas":
            print("welp")
        else:
            print("cool")
    print("you guys are off")
    print("you make it back safe and sound kinda")
    
else:
    print("bye")
        
