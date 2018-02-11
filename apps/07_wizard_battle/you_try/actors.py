import random

class Creature:
    def __init__(self, name,sound, minlevel=1,maxlevel=100, domain="A dark and foggy forest"):
        self.name =name 
        self.level=random.randint(minlevel,maxlevel)
        self.domain = domain
        self.sound = sound

    def __repr__(self):
        return "{} of level {} in {}".format(self.name,self.level, self.domain)

    def get_defensive_roll(self):
        return random.randint(1,12)  * self.level
    

class Wizard(Creature):

    def attack(self, other_creature):
        print("The Wizard {} attacks the {}.".format(self.name,other_creature.name))
        
        my_roll = self.get_defensive_roll()
        print("You rolled {}...".format(my_roll))

        creature_roll =other_creature.get_defensive_roll()
        print("The {} rolls {}...".format(other_creature.name, creature_roll))

        if my_roll<=creature_roll: 
            print("The {} has defeated {}".format(other_creature.name,self.name))
            return False
        else:
            print("{} has triumphed over the {}".format(self.name,other_creature.name))
            return True

class Dragon(Creature):
    def __init__(self, name, sound,scale_thinkness, breathes_fire,minlevel = 1, maxlevel = 100, domain = 'A dark and foggy forest'):
        self.breathes_fire=breathes_fire
        self.scale_thickness = scale_thinkness
        super().__init__(name, sound, minlevel, maxlevel, domain)
        

    def get_defensive_roll(self):
        base_roll = super().get_defensive_roll()
        fire_modifier = 5 if self.breathes_fire else 1
        scale_modifier = self.scale_thickness /10
        return base_roll * fire_modifier * scale_modifier


class SmallAnimal(Creature):
    def get_defensive_roll(self):
        base_roll = super().get_defensive_roll()
        return base_roll/2

