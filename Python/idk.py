import random

# Define the different rooms and their actions
rooms = {
    "Entrance": {
        "description": "You stand at the entrance of a dark dungeon. There are paths to the left and right.",
        "options": ["Go left", "Go right"],
        "left": "Trap Room",
        "right": "Treasure Room"
    },
    "Trap Room": {
        "description": "You enter a room filled with spikes on the floor. There is a door ahead and a passage back.",
        "options": ["Move ahead carefully", "Go back"],
        "ahead": "Monster Room",
        "back": "Entrance"
    },
    "Treasure Room": {
        "description": "You find a room filled with glittering treasure! Congratulations, you win!",
        "options": ["Take treasure", "Go back"],
        "back": "Entrance"
    },
    "Monster Room": {
        "description": "A fierce monster blocks your way! You can try to fight it or flee.",
        "options": ["Fight", "Run"],
        "fight": "Fight Outcome",
        "run": "Trap Room"
    },
    "Fight Outcome": {
        "description": "You prepare for battle!",
        "options": ["Attack", "Defend"],
    }
}

# Functions to handle different outcomes
def fight_monster():
    print("You attack the monster!")
