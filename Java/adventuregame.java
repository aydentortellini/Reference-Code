import java.util.*;

public class adventuregame {

    // ==================== ITEM CLASS ====================
    static class Item {
        String name;
        String description;
        boolean isWeapon;
        int damage;

        Item(String name, String description, boolean isWeapon, int damage) {
            this.name = name;
            this.description = description;
            this.isWeapon = isWeapon;
            this.damage = damage;
        }
    }

    // ==================== ENEMY CLASS ====================
    static class Enemy {
        String name;
        int health;
        int damage;
        String description;

        Enemy(String name, int health, int damage, String description) {
            this.name = name;
            this.health = health;
            this.damage = damage;
            this.description = description;
        }

        boolean isAlive() {
            return health > 0;
        }
    }

    // ==================== ROOM CLASS ====================
    static class Room {
        String name;
        String description;
        Map<String, Room> exits = new HashMap<>();
        List<Item> items = new ArrayList<>();
        Enemy enemy;
        boolean isLocked;
        String requiredKey;

        Room(String name, String description) {
            this.name = name;
            this.description = description;
            this.isLocked = false;
            this.requiredKey = null;
        }

        void addExit(String direction, Room room) {
            exits.put(direction.toLowerCase(), room);
        }

        void addItem(Item item) {
            items.add(item);
        }

        void describe() {
            System.out.println("\n========================================");
            System.out.println("📍 " + name);
            System.out.println("========================================");
            System.out.println(description);

            if (enemy != null && enemy.isAlive()) {
                System.out.println("\n⚠️  WARNING: " + enemy.description);
            }

            if (!items.isEmpty()) {
                System.out.println("\nYou see:");
                for (Item item : items) {
                    System.out.println("  • " + item.name + " - " + item.description);
                }
            }

            System.out.println("\nExits: " + String.join(", ", exits.keySet()));
        }
    }

    // ==================== PLAYER CLASS ====================
    static class Player {
        int health = 100;
        int maxHealth = 100;
        List<Item> inventory = new ArrayList<>();
        Room currentRoom;

        void showStatus() {
            System.out.println("\n❤️  Health: " + health + "/" + maxHealth);
            System.out.println("🎒 Inventory: " + (inventory.isEmpty() ? "Empty" : ""));
            for (Item item : inventory) {
                System.out.println("  • " + item.name + (item.isWeapon ? " (Weapon - " + item.damage + " dmg)" : ""));
            }
        }

        boolean hasItem(String itemName) {
            return inventory.stream().anyMatch(i -> i.name.equalsIgnoreCase(itemName));
        }

        Item getWeapon() {
            return inventory.stream().filter(i -> i.isWeapon).findFirst().orElse(null);
        }

        void heal(int amount) {
            health = Math.min(health + amount, maxHealth);
            System.out.println("💚 You healed for " + amount + " HP! Health: " + health + "/" + maxHealth);
        }
    }

    // ==================== GAME VARIABLES ====================
    static Scanner scanner = new Scanner(System.in);
    static Player player = new Player();
    static boolean gameRunning = true;
    static boolean hasEscaped = false;
    static int monstersDefeated = 0;

    // ==================== MAIN METHOD ====================
    public static void main(String[] args) {
        printTitle();
        setupGame();

        System.out.println("\nYou wake up in a dark, dusty room. The last thing you remember");
        System.out.println("is accepting a dare to spend the night in the abandoned Blackwood Mansion.");
        System.out.println("Now you need to find a way out... if you can survive.");
        System.out.println("\nType 'help' for a list of commands.\n");

        player.currentRoom.describe();

        while (gameRunning && player.health > 0) {
            System.out.print("\n> ");
            String input = scanner.nextLine().trim().toLowerCase();
            processCommand(input);
        }

        showEnding();
    }

    // ==================== GAME SETUP ====================
    static void setupGame() {
        // Create all rooms
        Room foyer = new Room("Foyer",
            "A grand entrance hall covered in cobwebs. A broken chandelier hangs overhead.\n" +
            "Faded portraits line the walls, their eyes seeming to follow you.");

        Room livingRoom = new Room("Living Room",
            "Dusty furniture is covered with white sheets. A fireplace crackles with an\n" +
            "unnatural green flame. Something moves in the shadows...");

        Room kitchen = new Room("Kitchen",
            "Rotten food and rusty utensils litter the counters. The smell is unbearable.\n" +
            "A door leads to what appears to be a cellar.");

        Room library = new Room("Library",
            "Towering bookshelves reach to the ceiling. Ancient tomes and scrolls are\n" +
            "scattered everywhere. A strange symbol is drawn on the floor.");

        Room cellar = new Room("Cellar",
            "A damp, cold underground room. Barrels and crates are stacked against the walls.\n" +
            "You hear scratching sounds coming from the darkness.");

        Room masterBedroom = new Room("Master Bedroom",
            "A luxurious but decayed bedroom. The four-poster bed has tattered curtains.\n" +
            "A vanity mirror shows a reflection that doesn't quite match reality...");

        Room attic = new Room("Attic",
            "Dusty boxes and forgotten memories fill this cramped space.\n" +
            "Moonlight streams through a broken window. You can see the front gate from here!");

        Room secretPassage = new Room("Secret Passage",
            "A hidden tunnel behind the bookshelf! The walls are covered in strange markings.\n" +
            "This leads directly to the mansion's exit!");

        // Connect rooms
        foyer.addExit("north", livingRoom);
        foyer.addExit("east", kitchen);
        foyer.addExit("west", library);

        livingRoom.addExit("south", foyer);
        livingRoom.addExit("up", masterBedroom);

        kitchen.addExit("west", foyer);
        kitchen.addExit("down", cellar);

        library.addExit("east", foyer);
        library.addExit("secret", secretPassage);  // Hidden exit

        cellar.addExit("up", kitchen);

        masterBedroom.addExit("down", livingRoom);
        masterBedroom.addExit("up", attic);

        attic.addExit("down", masterBedroom);

        secretPassage.addExit("back", library);
        secretPassage.addExit("exit", null);  // Winning exit!

        // Lock certain rooms
        masterBedroom.isLocked = true;
        masterBedroom.requiredKey = "rusty key";

        secretPassage.isLocked = true;
        secretPassage.requiredKey = "ancient tome";

        // Add items
        foyer.addItem(new Item("flashlight", "A flickering flashlight. Better than nothing.", false, 0));
        kitchen.addItem(new Item("kitchen knife", "A sharp but rusty knife.", true, 20));
        kitchen.addItem(new Item("moldy bread", "Disgusting, but might restore some health.", false, 0));
        cellar.addItem(new Item("rusty key", "An old key with a skull design.", false, 0));
        library.addItem(new Item("ancient tome", "A book titled 'Secrets of Blackwood'. The pages glow faintly.", false, 0));
        masterBedroom.addItem(new Item("silver dagger", "An ornate dagger with mystical engravings.", true, 35));
        attic.addItem(new Item("health potion", "A dusty bottle with a red liquid inside.", false, 0));

        // Add enemies
        livingRoom.enemy = new Enemy("Shadow Creature", 40, 15,
            "A Shadow Creature lurks in the corner, its red eyes fixed on you!");

        cellar.enemy = new Enemy("Giant Rat", 25, 10,
            "A Giant Rat the size of a dog hisses at you!");

        masterBedroom.enemy = new Enemy("Vengeful Spirit", 60, 20,
            "A Vengeful Spirit of the mansion's former owner blocks your path!");

        // Set starting room
        player.currentRoom = foyer;
    }

    // ==================== COMMAND PROCESSING ====================
    static void processCommand(String input) {
        if (input.isEmpty()) return;

        String[] parts = input.split(" ", 2);
        String command = parts[0];
        String argument = parts.length > 1 ? parts[1] : "";

        switch (command) {
            case "help":
                showHelp();
                break;
            case "look":
                player.currentRoom.describe();
                break;
            case "go":
            case "move":
            case "walk":
                move(argument);
                break;
            case "north":
            case "south":
            case "east":
            case "west":
            case "up":
            case "down":
            case "secret":
            case "exit":
            case "back":
                move(command);
                break;
            case "take":
            case "grab":
            case "pick":
                takeItem(argument);
                break;
            case "use":
                useItem(argument);
                break;
            case "inventory":
            case "inv":
            case "i":
                player.showStatus();
                break;
            case "attack":
            case "fight":
            case "kill":
                attack();
                break;
            case "examine":
            case "inspect":
                examine(argument);
                break;
            case "quit":
            case "exit game":
                gameRunning = false;
                System.out.println("Thanks for playing!");
                System.exit(0);
                break;
            default:
                System.out.println("I don't understand '" + input + "'. Type 'help' for commands.");
        }
    }

    // ==================== GAME ACTIONS ====================
    static void move(String direction) {
        if (direction.isEmpty()) {
            System.out.println("Go where? Try: go north, go south, go east, go west, go up, go down");
            return;
        }

        // Check if enemy is blocking
        if (player.currentRoom.enemy != null && player.currentRoom.enemy.isAlive()) {
            System.out.println("❌ The " + player.currentRoom.enemy.name + " blocks your escape! You must fight or die!");
            return;
        }

        Room nextRoom = player.currentRoom.exits.get(direction.toLowerCase());

        if (nextRoom == null && direction.equals("exit")) {
            // Winning condition!
            hasEscaped = true;
            gameRunning = false;
            return;
        }

        if (nextRoom == null) {
            System.out.println("You can't go that way.");
            return;
        }

        // Check if room is locked
        if (nextRoom.isLocked) {
            if (player.hasItem(nextRoom.requiredKey)) {
                System.out.println("🔓 You use the " + nextRoom.requiredKey + " to unlock the passage!");
                nextRoom.isLocked = false;
            } else {
                System.out.println("🔒 This way is locked. You need something to open it...");
                return;
            }
        }

        player.currentRoom = nextRoom;
        player.currentRoom.describe();

        // Enemy attacks when entering room
        if (player.currentRoom.enemy != null && player.currentRoom.enemy.isAlive()) {
            System.out.println("\n⚔️  The " + player.currentRoom.enemy.name + " attacks you!");
            player.health -= player.currentRoom.enemy.damage / 2;
            System.out.println("💔 You take " + (player.currentRoom.enemy.damage / 2) + " damage! Health: " + player.health);
        }
    }

    static void takeItem(String itemName) {
        if (itemName.isEmpty()) {
            System.out.println("Take what?");
            return;
        }

        // Check if enemy is present
        if (player.currentRoom.enemy != null && player.currentRoom.enemy.isAlive()) {
            System.out.println("❌ You can't focus on looting while the " + player.currentRoom.enemy.name + " threatens you!");
            return;
        }

        for (Item item : player.currentRoom.items) {
            if (item.name.toLowerCase().contains(itemName.toLowerCase())) {
                player.inventory.add(item);
                player.currentRoom.items.remove(item);
                System.out.println("✅ You picked up: " + item.name);
                return;
            }
        }
        System.out.println("There's no '" + itemName + "' here.");
    }

    static void useItem(String itemName) {
        if (itemName.isEmpty()) {
            System.out.println("Use what?");
            return;
        }

        for (Item item : player.inventory) {
            if (item.name.toLowerCase().contains(itemName.toLowerCase())) {
                if (item.name.contains("bread")) {
                    player.heal(15);
                    player.inventory.remove(item);
                    System.out.println("🤢 Disgusting... but you feel slightly better.");
                    return;
                } else if (item.name.contains("potion")) {
                    player.heal(50);
                    player.inventory.remove(item);
                    System.out.println("✨ The potion fills you with renewed energy!");
                    return;
                } else {
                    System.out.println("You can't use that item directly.");
                    return;
                }
            }
        }
        System.out.println("You don't have '" + itemName + "'.");
    }

    static void attack() {
        Enemy enemy = player.currentRoom.enemy;

        if (enemy == null || !enemy.isAlive()) {
            System.out.println("There's nothing to attack here.");
            return;
        }

        Item weapon = player.getWeapon();
        int damage = weapon != null ? weapon.damage : 5;  // Fists do 5 damage

        System.out.println("\n⚔️  COMBAT ⚔️");

        if (weapon != null) {
            System.out.println("You attack with your " + weapon.name + "!");
        } else {
            System.out.println("You swing your fists desperately!");
        }

        enemy.health -= damage;
        System.out.println("💥 You deal " + damage + " damage to the " + enemy.name + "!");

        if (enemy.isAlive()) {
            System.out.println("👹 " + enemy.name + " has " + enemy.health + " HP remaining!");
            player.health -= enemy.damage;
            System.out.println("💔 The " + enemy.name + " strikes back for " + enemy.damage + " damage!");
            System.out.println("❤️  Your health: " + player.health + "/" + player.maxHealth);
        } else {
            System.out.println("☠️  You defeated the " + enemy.name + "!");
            monstersDefeated++;
        }
    }

    static void examine(String target) {
        if (target.isEmpty()) {
            System.out.println("Examine what?");
            return;
        }

        // Check room items
        for (Item item : player.currentRoom.items) {
            if (item.name.toLowerCase().contains(target.toLowerCase())) {
                System.out.println("📖 " + item.name + ": " + item.description);
                if (item.isWeapon) {
                    System.out.println("   Damage: " + item.damage);
                }
                return;
            }
        }

        // Check inventory
        for (Item item : player.inventory) {
            if (item.name.toLowerCase().contains(target.toLowerCase())) {
                System.out.println("📖 " + item.name + ": " + item.description);
                if (item.isWeapon) {
                    System.out.println("   Damage: " + item.damage);
                }
                return;
            }
        }

        System.out.println("You don't see anything special about that.");
    }

    static void showHelp() {
        System.out.println("\n╔════════════════════════════════════════╗");
        System.out.println("║           AVAILABLE COMMANDS           ║");
        System.out.println("╠════════════════════════════════════════╣");
        System.out.println("║ Movement:                              ║");
        System.out.println("║   north, south, east, west, up, down   ║");
        System.out.println("║   go [direction]                       ║");
        System.out.println("╠════════════════════════════════════════╣");
        System.out.println("║ Actions:                               ║");
        System.out.println("║   look      - Examine the room         ║");
        System.out.println("║   take [x]  - Pick up an item          ║");
        System.out.println("║   use [x]   - Use an item              ║");
        System.out.println("║   examine [x] - Look at something      ║");
        System.out.println("║   attack    - Fight an enemy           ║");
        System.out.println("║   inventory - Check your items         ║");
        System.out.println("║   quit      - Exit the game            ║");
        System.out.println("╚════════════════════════════════════════╝");
    }

    // ==================== ENDINGS ====================
    static void showEnding() {
        System.out.println("\n");
        System.out.println("════════════════════════════════════════");

        if (player.health <= 0) {
            System.out.println("           💀 GAME OVER 💀");
            System.out.println("════════════════════════════════════════");
            System.out.println("The darkness consumes you...");
            System.out.println("Your body is never found.");
            System.out.println("\nMonsters defeated: " + monstersDefeated);
        } else if (hasEscaped) {
            if (monstersDefeated >= 3) {
                System.out.println("         🏆 PERFECT ENDING 🏆");
                System.out.println("════════════════════════════════════════");
                System.out.println("You escaped the mansion AND defeated all");
                System.out.println("the horrors within! The curse is broken!");
                System.out.println("\nYou are a TRUE SURVIVOR!");
            } else if (monstersDefeated >= 1) {
                System.out.println("          ⭐ GOOD ENDING ⭐");
                System.out.println("════════════════════════════════════════");
                System.out.println("You escaped Blackwood Mansion alive!");
                System.out.println("The nightmares will haunt you forever,");
                System.out.println("but at least you survived.");
            } else {
                System.out.println("          😰 ESCAPE ENDING 😰");
                System.out.println("════════════════════════════════════════");
                System.out.println("You fled the mansion in terror!");
                System.out.println("You survived... barely. But the evil");
                System.out.println("still lurks within those walls.");
            }
            System.out.println("\nMonsters defeated: " + monstersDefeated);
            System.out.println("Final health: " + player.health + "/" + player.maxHealth);
        }

        System.out.println("════════════════════════════════════════");
        System.out.println("      Thanks for playing!");
        System.out.println("════════════════════════════════════════");
    }

    static void printTitle() {
        System.out.println("╔═══════════════════════════════════════════════════════════╗");
        System.out.println("║                                                           ║");
        System.out.println("║    ▄▄▄▄    ██▓    ▄▄▄       ▄████▄   ██ ▄█▀              ║");
        System.out.println("║   ▓█████▄ ▓██▒   ▒████▄    ▒██▀ ▀█   ██▄█▒               ║");
        System.out.println("║   ▒██▒ ▄██▒██░   ▒██  ▀█▄  ▒▓█    ▄ ▓███▄░               ║");
        System.out.println("║   ▒██░█▀  ▒██░   ░██▄▄▄▄██ ▒▓▓▄ ▄██▒▓██ █▄               ║");
        System.out.println("║   ░▓█  ▀█▓░██████▒▓█   ▓██▒▒ ▓███▀ ░▒██▒ █▄              ║");
        System.out.println("║                                                           ║");
        System.out.println("║              ░██╗    ██╗ ██████╗  ██████╗ ██████╗         ║");
        System.out.println("║              ░██║    ██║██╔═══██╗██╔═══██╗██╔══██╗        ║");
        System.out.println("║              ░██║ █╗ ██║██║   ██║██║   ██║██║  ██║        ║");
        System.out.println("║              ░██║███╗██║██║   ██║██║   ██║██║  ██║        ║");
        System.out.println("║              ░╚███╔███╔╝╚██████╔╝╚██████╔╝██████╔╝        ║");
        System.out.println("║                                                           ║");
        System.out.println("║             🏚️  BLACKWOOD MANSION 🏚️                      ║");
        System.out.println("║                                                           ║");
        System.out.println("╚═══════════════════════════════════════════════════════════╝");
    }
}
