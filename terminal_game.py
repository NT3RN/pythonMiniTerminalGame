import random

def spacebattle(player):
    alienHp = random.randint(20,33)
    print('Hostile a alien ship detected')
    while player['hp']>0 and alienHp > 0:
        print(f'''Ship integrity {player['hp']}
            1. Lasser attack
            2. Plasma Sheild
            3. Heal''')
        choice = input('Choose action (1-3): ')
        # Player Turn
        shield_active = False
        if choice == '1':
            damage = random.randint(5, 12)
            alienHp -= damage
            print(f"You fired lasers! Alien took {damage} damage.")
        elif choice == '2':
            shield_active = True
            print("Plasma Shield activated!")
        elif choice == '3':
            heal = random.randint(5, 10)
            player['hp'] += heal
            print(f"Repairs complete. Integrity increased by {heal}.")
        else:
            print("Invalid command! You hesitated.")
        #Alien Turn
        if alienHp > 0:
            alien_damage = random.randint(5, 15)
            if shield_active:
                print("Your shield blocked the alien's attack!")
            else:
                player['hp'] -= alien_damage
                print(f"Alien fired back! You took {alien_damage} damage.")
    if player['hp'] > 0:
        print("\nTARGET DESTROYED")
        return True
    else:
        print("\nCRITICAL FAILURE!")
        return False
def adventure():
    player = {"hp": 90}
    print("Galactic Exploration Mission")
    print("You command a small exploration vessel on the edge of uknown space.\n")

    print("Where do you jump next?")
    print("1. Nebula X-69")
    print("2. Derelict Space Station")

    choice = input('Enter 1 or 2: ')
    if choice == '1':
        print('Your ship is entering the nebula')
        if not spacebattle(player):
            print('Your ship was destroyed in the nebula')
            return
    elif choice == '2':
        print('You docked with a abandonded station\nYou salvage parts for the ship. Ship integrity +10')
        player["hp"] += 10
    else:
        print('Navigation error. Lost in the space')
        return 
    
    print('''Ship\'s scanner detected an alien mothership
                1. Engage the mothership
                2. Jump to hyperspace and escape''')
    final = input('Choose: ')
    if final != '1' and final != '2':
        final = input('Choose: ')
    if final == '1':
        print('Final battle started')
        if spacebattle(player):
            print('Mothership is destroyed the galaxy is safe.')
        else:
            print('Your ship was destroyed. Mission failed')
    else:
        print('Jumped into hyperspace. Exploration continues')
        
adventure()