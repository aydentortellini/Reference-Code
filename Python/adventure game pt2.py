
import random
import time

def slow_print(text, delay=0.03):
    """Print text with a typing effect"""
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()

def get_player_details():
    """Collect player information and create character"""
    player = {
        'name': input("What is your name, brave adventurer? "),
        'health': 100,
        'food': 0,
        'inventory': [],
        'skills': [],
        'background': ''
    }
    
    slow_print("Welcome, " + player['name'] + "! Your adventure begins...")
    return player

def choose_background(player):
    """Allow player to choose a background story"""
    slow_print("\nChoose your background:")
    backgrounds = [
        "Wilderness Survivor",
        "Ex-Military Scout", 
        "Adventurous Researcher",
        "Local Jungle Guide"
    ]
    
    for i, background in enumerate(backgrounds, 1):
        print(str(i) + ". " + background)
    
    while True:
        try:
            choice = int(input("Enter the number of your background: "))
            if 1 <= choice <= len(backgrounds):
                player['background'] = backgrounds[choice-1]
                player['skills'].append(backgrounds[choice-1].lower().split()[1])
                break
            else:
                print("Invalid choice. Try again.")
        except ValueError:
            print("Please enter a number.")
    
    slow_print("You have chosen to be a " + player['background'] + "!")
    return player

def jungle_exploration(player):
    """Main jungle exploration sequence"""
    slow_print("\n--- JUNGLE EXPLORATION ---")
    slow_print("You find yourself deep in an uncharted jungle...")
    
    # Multiple exploration options
    exploration_options = [
        "Hunt for food",
        "Search for water",
        "Look for shelter",
        "Investigate strange sounds"
    ]
    
    for i, option in enumerate(exploration_options, 1):
        print(str(i) + ". " + option)
    
    choice = int(input("What would you like to do? "))
    
    if choice == 1:  # Hunting
        return hunting_mini_game(player)
    elif choice == 2:  # Water search
        return water_search(player)
    elif choice == 3:  # Shelter
        return find_shelter(player)
    elif choice == 4:  # Investigate sounds
        return investigate_sounds(player)

def hunting_mini_game(player):
    """Detailed hunting mini-game"""
    animals = [
        {"name": "Deer", "difficulty": 3, "food_value": 30},
        {"name": "Wild Boar", "difficulty": 5, "food_value": 50},
        {"name": "Turkey", "difficulty": 2, "food_value": 20}
    ]
    
    chosen_animal = random.choice(animals)
    slow_print("You spot a " + chosen_animal['name'] + "!")
    
    # Skill-based hunting
    hunting_success = random.randint(1, 10) + (3 if "scout" in player['skills'] or "guide" in player['skills'] else 0)
    
    if hunting_success >= chosen_animal['difficulty']:
        slow_print("Success! You successfully hunt the " + chosen_animal['name'] + "!")
        player['food'] += chosen_animal['food_value']
        player['inventory'].append(chosen_animal['name'] + " meat")
        slow_print("You gained " + str(chosen_animal['food_value']) + " food!")
    else:
        slow_print("The " + chosen_animal['name'] + " escapes. Better luck next time!")
    
    return player

def water_search(player):
    """Water searching mini-game"""
    water_sources = [
        {"type": "River", "quality": "Good", "health_boost": 20},
        {"type": "Muddy Pond", "quality": "Risky", "health_boost": -10},
        {"type": "Mountain Stream", "quality": "Excellent", "health_boost": 30}
    ]
    
    chosen_source = random.choice(water_sources)
    slow_print("You find a " + chosen_source['type'] + ". (" + chosen_source['quality'] + ")")
    
    if input("Drink from this source? (yes/no) ").lower() == 'yes':
        player['health'] += chosen_source['health_boost']
        slow_print("Health changed by " + str(chosen_source['health_boost']))
    
    return player

def find_shelter(player):
    """Shelter finding mini-game"""
    shelters = [
        {"type": "Cave", "protection": True},
        {"type": "Tree House", "protection": True},
        {"type": "Natural Rock Formation", "protection": False},
        {"type": "Dense Bush Cluster", "protection": False}
    ]
    
    chosen_shelter = random.choice(shelters)
    slow_print("You discover a(n) " + chosen_shelter['type'] + "!")

    if chosen_shelter['protection']:
        slow_print("The shelter protects you from potential dangers.")
        player['health'] += 10
    else:
        slow_print("The shelter offers minimal protection.")
        
    return player

def investigate_sounds(player):
    """Mysterious sounds investigation"""
    outcomes = [
        ("You find an abandoned research camp filled with old equipment.", True),
        ("A rare bird flies away, leaving you in awe.", False),
        ("You discover ancient tribal markings on the trees.", True),
        ("Something moves in the shadows... it's just a monkey!", False)
    ]
    
    outcome, found_item = random.choice(outcomes)
    
    slow_print(outcome)
    
    if found_item:
        item_found = random.choice(["Ancient Map", "Tribal Artifact"])
        player['inventory'].append(item_found)
        slow_print("You found an item: **" + item_found + "** and added it to your inventory!")
        
    return player

def final_encounter(player):
    """Final game encounter with scientists"""
    
    # The suspense builds as you stumble upon the scientists.
    slow_print("\n--- FINAL ENCOUNTER ---")
    slow_print("After a long day of exploration, you encounter a group of scientists preparing to leave the jungle.")
    
    scientists = ["Jacob", "Jake", "Alvin", "Calvin", "Nicholas"]
    chosen_scientists = random.sample(scientists, 3)
    
    print("Available scientists: ", ", ".join(chosen_scientists))
    
    pilot = input("Choose your pilot: ")
    while pilot not in chosen_scientists:
        pilot = input("Invalid choice. Choose again: ")
    
    slow_print(pilot + ", the pilot of this expedition, welcomes you aboard their helicopter.")
    slow_print("However, they mention that there is one more challenge before you can leave...")

    # Final challenge before escape
    final_challenge()

    return player

def final_challenge():
    """Final challenge before escaping the jungle"""
    challenges = [
        ("A sudden storm approaches! You must secure the helicopter before it gets damaged.", True),
        ("A wild animal appears! You need to scare it away.", False),
        ("The helicopter is running low on fuel! You must help refuel it.", True),
        ("One of the scientists is injured! You need to help them.", False)
    ]

    challenge, success_required = random.choice(challenges)

    slow_print(challenge)

    if success_required:
        success_roll = random.randint(1, 10)
        if success_roll > 5:
            slow_print("You successfully completed the challenge!")
        else:
            slow_print("Unfortunately, you failed to complete the challenge. The team is delayed.")
            # Optionally reduce health or food here.
    else:
        fail_roll = random.randint(1, 10)
        if fail_roll > 5:
            slow_print("You bravely scare away the wild animal!")
        else:
            slow_print("The animal charges at you! Fortunately, you manage to escape unharmed.")

def game_conclusion(player):
    """Conclude the game and show player stats"""
    slow_print("\n--- ADVENTURE SUMMARY ---")
    slow_print("Name: " + player['name'])
    slow_print("Background: " + player['background'])
    slow_print("Health: " + str(player['health']))
    slow_print("Food Collected: " + str(player['food']))
    slow_print("Inventory: " + ", ".join(player['inventory'] or ["Empty"]))
    
    if player['health'] > 0:
        slow_print("\nCongratulations! You have survived your adventure and made it back safely!")
    else:
        slow_print("\nSadly, your journey has come to an end...")

def main():
    """Main game loop"""
    player = get_player_details()
    player = choose_background(player)
    
    # Multiple exploration rounds
    for round in range(3):
        player = jungle_exploration(player)
        
        if player['health'] <= 0:
            break
    
    if player['health'] > 0:
        final_encounter(player)

    game_conclusion(player)

if __name__ == "__main__":
    main()
