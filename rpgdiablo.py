import random

logo = """

█▀▄▀█ █ █▄░█ █ ▄▄ █▀▄ █ ▄▀█ █▄▄ █░░ █▀█
█░▀░█ █ █░▀█ █ ░░ █▄▀ █ █▀█ █▄█ █▄▄ █▄█
"""

class Player:
    def __init__(self, class_type, name):
        self.name = name
        self.class_type = class_type
        self.hp = 100
        if class_type == "Barbarian":
            self.attack_damage = 15
            self.special = "Berseker"
        elif class_type == "Sorcerer":
            self.attack_damage = 10
            self.special = "Fireball"
        elif class_type == "Paladin":
            self.attack_damage = 12
            self.special = "Holy Bolt"

    def attack(self, target):
        damage = self.attack_damage
        print(f"You dealt {damage} damage to {target.name}!")
        target.hp -= damage

    def special_attack(self, target):
        damage = self.attack_damage * 2
        print(f"You dealt {damage} damage to {target.name}!")
        target.hp -= damage
    
    def heal(self):
        heal_amount = random.randint(10, 20)
        self.hp += heal_amount
        print(f"You healed for {heal_amount} HP!")

class Enemy:
    def __init__(self, name):
        self.name = name
        self.hp = random.randint(20, 40)


    def attack(self, target):
        damage = random.randint(5, 10)
        print(f"{self.name} dealt {damage} damage to {target.name}!")
        target.hp -= damage

def choose_class():
    player_name = input("Enter your character's name: ")
    print("Choose your class:\n1. Barbarian\n2. Sorcerer\n3. Paladin")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        return Player("Barbarian", player_name)
    elif choice == 2:
        return Player("Sorcerer", player_name)
    elif choice == 3:
        return Player("Paladin", player_name)
    else:
        print("Invalid choice. Please try again.")
        return choose_class()


def encounter(player):
    enemy = Enemy("Demon")
    print(f"A wild {enemy.name} has appeared!")
    while enemy.hp > 0 and player.hp > 0:
        action = input("Choose your action: Attack (a) Special Attack (s) or Heal (h)? ")
        if action == 'a':
            player.attack(enemy)
        elif action == 's':
            player.special_attack(enemy)
        elif action == 'h':
            player.heal()
        else:
            print("Invalid action. Please try again.")
            continue

        if enemy.hp > 0:
            enemy.attack(player)


        print(f"Your HP: {player.hp} | Enemy HP: {enemy.hp}")

        if player.hp <= 0:
            print("You have been defeated by the Demon. Game Over.")
            return
        elif enemy.hp <= 0:
            print("You have defeated the Demon. You win!")
            break

def main():
    print(logo)
    print("Welcome to Mini-Diablo: Quest for the Sacred Stones!")
    player = choose_class()
    print(f"You have chosen the path of the {player.class_type}.")

    encounter(player)

if __name__ == "__main__":
    main()
