from actors import Wizard,Creature, Dragon, SmallAnimal
import random
import time

def main():
    print_header()
    game_loop()

def print_header():
    print("---------------------------------")
    print("            Wizard game")
    print("---------------------------------")
    print()


def game_loop():
    
    creatures = [
        SmallAnimal('Toad','croaks',1,3, "the pool skimmer"),
        Creature('Tiger','growls',12,20),
        SmallAnimal('Bat','squeaks',3,9, "a cave"),
        Dragon('Dragon','roars',3,True,50,150, "it's mountainous lair"),
        Wizard('Evil Wizard','yells',500,550,"a spooky castle"),
    ]

    hero = Wizard("Gandalf",750)

    while True:

        active_creature = random.choice(creatures)
        print("\nA {} has appeared from {} and {} at you.\n".format(active_creature,active_creature.domain,active_creature.sound))

        cmd= str.lower(input("Do you [a]ttack, [r]unaway, [l]ook around, or [q]uit?"))
   
        if cmd =="a":
            if hero.attack(active_creature):
                creatures.remove(active_creature)
            else:
                print("{} runs and hides taking time to recover...".format(hero.name))
                time.sleep(3)
                print("{} has returned revitalized".format(hero.name))                                
            
        elif cmd=="r":
            print("{} has become unsure and flees".format(hero.name))

        elif cmd=="l":
            print("Creatures Left:")
            for c in creatures:
                print("A {}".format(c))

        elif cmd=="q":
            print("Goodbye")
            break
        else:
            print("I don't understand the command {}".format(cmd))

        if not creatures:
            print("You defeated all of the creatures and won the game!")
            break
        
if __name__ == "__main__": 
    main()