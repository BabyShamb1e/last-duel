"""
1vs1 duel game!
"""
import random

MIN_DAMAGE = 1
MAX_DAMAGE = 99

def main():
    print("-------------------------------------------------------------------")
    print("This game is for 2 players fighting each other, until one man left.") 
    print("Each player has 35 health at the start.")
    print("There are 3 weapons to choose from: 'sword', 'axe' and 'bow'.")
    print("Every weapon has its own damage and a miss chance.")
    print("You must type in one of the weapons to deal damage")
    print("-------------------------------------------------------------------")
#Defining how much health do players have:
    health1 = 35
    health2 = 35
#Meeting
    name1 = input("What is your name, fellow stranger? ")
    name2 = input("What is your name, fellow stranger? ")
    print()
#Game continues until this happens 
    while health1 or health2 != 0:
#First player attacks
        health2 = attack1(health2, name1) 
        print(name2 +  " has " + str(health2) + " health left.")
        print()
#Conditional to win the game for the first player
        if health2 <= 0:
            print(name2 + " has died 💀")
            print(name1 + " wins!🎉🎉🎉")
            break
#Second player attacks
        health1 = attack2(health1, name2)
        print(name1 + " has " + str(health1) + " health left.")
        print()
#Conditional to win the game for the second player
        if health1 <= 0:
            print(name1 + " has died 💀")
            print(name2 + " wins!🎉🎉🎉")
            break


#Defining amount of damage and miss chance for all the weapons
def attack1(health2, name1):
    atq1 = input(name1 + " choose a weapon: ")
    while atq1 not in ['sword', 'axe', 'bow', 'ugotpwnd']:
        print('Hey, choose a weapon among: sword, axe or bow')
        atq1 = input()
#Sword mechanics
    if atq1 == 'sword':
        sword = random.randint(5,7)
        damage = random.randint(MIN_DAMAGE, MAX_DAMAGE)
        if damage >= 85:
            print("Miss...")
            return health2
        else:
            print("You dealt " + str(sword) + " 🗡️ damage. ")
            return health2 - sword
#Axe mechanics
    elif atq1 == 'axe':
        axe = random.randint(7,11)
        damage = random.randint(MIN_DAMAGE, MAX_DAMAGE)
        if damage >= 65:
            print("Miss...")
            return health2
        else:
            print("You dealt " + str(axe) + " ⛏️ damage. ")
            return health2 - axe
#Bow mechanics
    elif atq1 == 'bow':
        bow = random.randint(11,19)
        damage = random.randint(MIN_DAMAGE, MAX_DAMAGE)
        if damage >= 20:
            print("Miss... ")
            return health2
        else:
            print("You dealt " + str(bow) + " 🏹 damage. ")
            return health2 - bow
#Cheats
    elif atq1 == "ugotpwnd":
        cheat = 99
        print(name1 + " dealt 99 damage with a fireball! 🔥")
        return health2 - cheat

#Defining amount of damage and miss chance  for all the weapons
def attack2(health1, name2):
    atq2 = input(name2 + " choose a weapon: ")
    while atq2 not in ['sword', 'axe', 'bow', 'ugotpwnd']:
        print('Hey, choose a weapon among: sword, axe or bow')
        atq2 = input()
#Sword mechanics
    if atq2 == 'sword':
        sword = random.randint(5,7)
        damage = random.randint(MIN_DAMAGE, MAX_DAMAGE)
        if damage >= 85:
            print("Miss...")
            return health1
        else:
            print("You dealt " + str(sword) + " 🗡️ damage. ")
            return health1 - sword
#Axe mechanics
    elif atq2 == 'axe':
        axe = random.randint(7,11)
        damage = random.randint(MIN_DAMAGE, MAX_DAMAGE)
        if damage >= 65:
            print("Miss...")
            return health1
        else:
            print("You dealt " + str(axe) + " ⛏️ damage. ")
            return health1 - axe
#Bow mechanics
    elif atq2 == 'bow':
        bow = random.randint(11,19)
        damage = random.randint(MIN_DAMAGE, MAX_DAMAGE)
        if damage >= 20:
            print("Miss... ")
            return health1
        else:
            print("You dealt " + str(bow) + " 🏹 damage. ")
            return health1 - bow
#Cheats
    elif atq2 == "ugotpwnd":
        cheat = 99
        print(name2 + " dealt 99 damage with a fireball! 🔥")
        return health1 - cheat
        

if __name__ == '__main__':
    main()