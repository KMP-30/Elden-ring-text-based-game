"""
Filename: elden_ring_adventure.py
Author: kavya purohit
Date: 20 January 2025
Description: AnvElden Ring-inspired text-based adventure with events where the player has to navigate through obstalces and finish different scenarios.
"""

# Importing necessary libraries
import random

# Initialize data structures
locations = {
    "Forbidden Forest": [
        "Follow the sound of rushing water",
        "Investigate the flickering lights in the distance"
    ],
    "Ruined Castle": [
        "Ascend the grand staircase",
        "Enter the dark hallway"
    ],
    "Sunken Catacombs": [
        "Follow the sound of distant chanting",
        "Explore the quiet tunnel"
    ]
}

events = {
    "Forbidden Forest": {
        "rushing water": {
            "description": "You find a glowing sword embedded in the rock.",
            "choices": ["Pull the sword", "Leave the sword"]
        },
        "flickering lights": {
            "description": "You find will-o'-the-wisps leading to an ancient tree.",
            "choices": ["Touch the tree", "Walk away"]
        }
    },
    "Ruined Castle": {
        "grand staircase": {
            "description": "At the top, you find a locked chest.",
            "choices": ["Open the chest", "Leave the chest"]
        },
        "dark hallway": {
            "description": "A spectral knight challenges you.",
            "choices": ["Fight the knight", "Flee"]
        }
    },
    "Sunken Catacombs": {
        "distant chanting": {
            "description": "You encounter a group of cultists performing a ritual.",
            "choices": ["Interrupt the ritual", "Observe from shadows"]
        },
        "quiet tunnel": {
            "description": "You discover a treasure vault guarded by traps.",
            "choices": ["Disarm traps", "Walk away"]
        }
    }
}

inventory = []

def main():
    """
    Main menu function that loops until the player chooses to quit.
    """
    print("""
    ⚔️ WELCOME TO THE LANDS BETWEEN ⚔️
    A desolate land filled with untold mysteries. Will you rise to become the Elden Lord?
    """)

    while True:
        print("\nChoose your path:")
        print("1. Enter the Forbidden Forest")
        print("2. Explore the Ruined Castle")
        print("3. Traverse the Sunken Catacombs")
        print("4. Check Inventory")
        print("5. Quit the Game")

        main_choice = input("> ").lower()

        if main_choice == "1":
            explore_location("Forbidden Forest")
        elif main_choice == "2":
            explore_location("Ruined Castle")
        elif main_choice == "3":
            explore_location("Sunken Catacombs")
        elif main_choice == "4":
            check_inventory()
        elif main_choice == "5":
            print("Farewell, Tarnished. May the flames guide thee.")
            break
        else:
            print("Invalid choice. Please select 1, 2, 3, 4, or 5.")

def explore_location(location):
    print(f"\n You arrive at the {location}.")
    print("Choose your action:")

    for i, action in enumerate(locations[location], 1):
        print(f"{i}. {action}")

    choice = input("> ").lower()

    if choice == "1":
        resolve_event(location, list(events[location].keys())[0])
    elif choice == "2":
        resolve_event(location, list(events[location].keys())[1])
    else:
        print("Invalid choice. Please select a valid action.")

def resolve_event(location, event_key):
    event = events[location][event_key]
    print(f"\n{event['description']}")

    for i, option in enumerate(event["choices"], 1):
        print(f"{i}. {option}")

    event_choice = input("> ").lower()

    if event_choice == "1":
        outcome = random.choice(["success", "failure"])
        if outcome == "success":
            print("You succeed and gain a new item.")
            inventory.append(f"Item from {event_key}")
        else:
            print("You fail and take damage.")
    elif event_choice == "2":
        print("You decide to move on cautiously.")
    else:
        print("Invalid choice. Please select 1 or 2.")

def check_inventory():
    print("\nYour inventory contains:")
    if inventory:
        for item in inventory:
            print(f"- {item}")
    else:
        print("- Nothing yet!")

# Run the game
if __name__ == "__main__":
    main()
