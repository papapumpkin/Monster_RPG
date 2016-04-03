import random

'''class Weapons:
    
    dmg_added = 0
    durability = 0
    range = 0
    
class Axe(Weapons):
    
    def __init__(self, **kwargs):
    
class Sword(Weapons):

    def __init__(self, **kwargs):
    
class Bow(Weapons):

    def __init__(self, **kwargs):
    
'''

class Combat: #  Contians attributes which pertain to combat interactions 
              #  betwen players and monsers     
    
    def attack(self): #  lets player or monster deal damage = to attk 
        damage_output = self.dmg 
        return damage_output

    def dodge_attempt(self): #  allows player attempt to avoid monster attack
        dodge = random.randint(1, 6)
        return dodge > 4
    #this doesn't work properly
            
        
    
    def rest(self): #  allows user to rest in order to regain health
        
        if self.current_hp == self.base_hp:
            print ("Your health is full already.")
            self.user_turn()
            
        else:       
            print("You chose to rest this turn")
        
            self.current_hp += 10
            
            if self.current_hp > 100:
                self.current_hp = 100

            print("HP: {}/{}".format(self.current_hp, self.base_hp))
            

#class Magic():     
        
class Monster(Combat): #defines basic attributes of generated monsters
    
    min_hp = 1  #min hp
    max_hp = 1  #max hp 
    min_dmg = 1  #min damage added to basic attacks
    max_dmg = 1  #max damage added to basic attacks
    min_exp = 1  #min amount of exp gained by character after killing monster
    max_exp = 1  #max amount of exp gained by character after killing monster
    min_armor = 0  #min float that lessens damage from basic attacks
    max_armor = 1  #max float that lessens damage from basic attacks
    spells = False  #whether or not the monster has access to special spells
    min_gold = 1  #min amount of gold dropped by monster on death
    max_gold = 1  #max amount of gold dropped by monster on death
    sound = 'roar' #shows sound monster makes
    sweet_spot_min = 0
    sweet_spot_max = 1  #creates a list used to determine the likely hood of inflicting extra damage
    

    def battlecry(self): #  prints noise monster makes
        print(self.sound.upper())
        
    def monster_turn(self, other): #  doesn't work properly
        print("You are being attacked.")
        dodger = input("Attempt to dodge? Y/n ").lower()
        if dodger == 'y':
            tof = other.dodge_attempt
            if tof == True:
                print("="*50)
                print("Attack dodged!")
                pass
                
            else:
                print("="*50)
                print("Dodge failed")
                attack = self.attack()
                other.current_hp -= attack
                return other.current_hp
                
        elif dodger == 'n':
            attack = self.attack()
            other.current_hp -= attack
            return other.current_hp
            
        else:
            print("="*50)
            print("Say what?")
            attack = self.attack()
            other.current_hp -= attack
            return other.current_hp
            
            
    
    def __str__(self): #  prints monster stats 
        return "HP: {}/{} XP: {} Amr: {}".format(self.current_hp, self.hp, self.exp, self.armor) 
        
    def suprise(self):  #  Determines whether or not Monster deals suprise damage to player at begining of encounter
        odds = list(range(0, 20))
        outcome = odds[random.randint(0, 19)]
        if outcome % 4 == 0:
            return True
            
        else:
            return False


class Grunt(Monster):
    max_hp = 3
    max_dmg = 2
    max_exp = 3
    max_armor = 0
    max_gold = 5
    sweet_spot_max = 5
    sound = 'gurble gurble'

    def __init__(self, **kwargs):  #  sets Grunt attributes to random number between given values
        self.hp = random.randint(self.min_hp, self.max_hp)
        self.current_hp = self.hp
        self.dmg = random.randint(self.min_dmg, self.max_dmg)
        self.exp = random.randint(self.min_exp, self.max_exp)
        self.armor = random.randint(self.min_armor, self.max_armor)
        self.gold = random.randint(self.min_gold, self.max_gold)
        self.sweet_spot = list(range(random.randint(self.sweet_spot_min, self.sweet_spot_max)))

        

class Goblin(Monster):
    max_hp = 5
    max_dmg = 3
    max_exp = 5
    max_armor = 1
    max_gold = 10
    sweet_spot_max = 10
    sound = 'hisssssssss'

    def __init__(self, **kwargs):
        self.hp = random.randint(self.min_hp, self.max_hp)
        self.current_hp = self.hp
        self.dmg = random.randint(self.min_dmg, self.max_dmg)
        self.exp = random.randint(self.min_exp, self.max_exp)
        self.armor = random.randint(self.min_armor, self.max_armor)
        self.gold = random.randint(self.min_gold, self.max_gold)
        self.sweet_spot = list(range(random.randint(self.sweet_spot_min, self.sweet_spot_max)))
        
        
class Ogre(Monster):
    min_hp = 3
    max_hp = 7
    min_dmg = 2
    max_dmg = 5
    min_exp = 5
    max_exp = 10
    max_armor = 5
    min_gold = 10
    max_gold = 20
    sweet_spot_max = 15
    sound = '{} smash!'.format('ogre')

    def __init__(self, **kwargs):
        self.hp = random.randint(self.min_hp, self.max_hp)
        self.current_hp = self.hp
        self.dmg = random.randint(self.min_dmg, self.max_dmg)
        self.exp = random.randint(self.min_exp, self.max_exp)
        self.armor = random.randint(self.min_armor, self.max_armor)
        self.gold = random.randint(self.min_gold, self.max_gold)
        self.sweet_spot = list(range(random.randint(self.sweet_spot_min, self.sweet_spot_max)))
        
        

class DarkElf(Monster):
    min_hp = 5
    max_hp = 10
    min_dmg = 5
    max_dmg = 10
    min_exp = 20 
    max_exp = 50
    min_armor = 0
    max_armor = 0
    min_gold = 20
    max_gold = 50
    sweet_spot_max = 50
    spells = True
    sound = 'e pluribus unum'

    def __init__(self, **kwargs):
        self.hp = random.randint(self.min_hp, self.max_hp)
        self.current_hp = self.hp
        self.dmg = random.randint(self.min_dmg, self.max_dmg)
        self.exp = random.randint(self.min_exp, self.max_exp)
        self.armor = random.randint(self.min_armor, self.max_armor)
        self.gold = random.randint(self.min_gold, self.max_gold)
        self.sweet_spot = list(range(random.randint(self.sweet_spot_min, self.sweet_spot_max)))
        

class Dragon(Monster):
    min_hp = 10
    max_hp = 20
    min_dmg = 5
    max_dmg = 10
    min_exp = 50
    max_exp = 100
    min_armor = 5
    max_armor = 10
    min_gold = 50
    max_gold = 100
    sweet_spot_max = 20
    sound = 'raaaaaaar'

    def __init__(self, **kwargs):
        self.hp = random.randint(self.min_hp, self.max_hp)
        self.current_hp = self.hp
        self.dmg = random.randint(self.min_dmg, self.max_dmg)
        self.exp = random.randint(self.min_exp, self.max_exp)
        self.armor = random.randint(self.min_armor, self.max_armor)
        self.gold = random.randint(self.min_gold, self.max_gold)
        self.sweet_spot = list(range(random.randint(self.sweet_spot_min, self.sweet_spot_max)))
        
    

class Necromancer(Monster):
    min_hp = 4
    max_hp = 10
    min_dmg = 20
    max_dmg = 40
    max_exp = 100
    min_armor = 0
    max_armor = 0
    min_gold = 50
    max_gold = 100
    sweet_spot_max = 100
    spells = True
    sound = 'the dead will rise!'

    def __init__(self, **kwargs):
        self.hp = random.randint(self.min_hp, self.max_hp)
        self.current_hp = self.hp
        self.dmg = random.randint(self.min_dmg, self.max_dmg)
        self.exp = random.randint(self.min_exp, self.max_exp)
        self.armor = random.randint(self.min_armor, self.max_armor)
        self.gold = random.randint(self.min_gold, self.max_gold)
        self.sweet_spot = list(range(random.randint(self.sweet_spot_min, self.sweet_spot_max)))
        

            
            
class Character(Combat): #  sets attributes of the person playing the game
    
    base_hp = 100 #character hp
    current_hp = 100
    dmg = 1 # damage added to basic attacks
    exp = 0 #  how much exp character currently has
    level = 1 #  current level
    exp_count = 5 #  how much exp is needed to level up
    armor = '' #  armor item that has float attribute that lessens damage from basic attacks
    spells = False #  whether or not character has access to special spells
    gold = 0
    name = '' #  name of character
    weapon = '' #  weapon character has


    def get_weapon(self): #  allows player to choose a weapon
         
        self.weapon = input("""
Select a weapon:
[A]xe
[B]ow
[S]word
> """).lower() # bad syntax
        if self.weapon == 'a':
            self.weapon = 'Axe'
            return self.weapon
            
        elif self.weapon == 'b':
            self.weapon = 'Bow'
            return self.weapon
            
        elif self.weapon == 's':
            self.weapon = 'Sword'
            return self.weapon
            
        else:
            print('That is not a valid choice.')
            self.weapon = self.get_weapon()
        

        
    def user_turn(self, other): # lets user choose which action to take on turn
    
        print("Do what on your turn?")
        choice = input('[A]ttack  [R]est  [S]pell > ').lower()
        print('='*50)
        print('\n')
        
        if choice == 'a':
            attack = self.attack()
            print("you dealt {} damage to the Monster.".format(attack))
            other.current_hp -= attack
            return other.current_hp
                
                
        elif choice == 'r':
            self.rest()
            
            
        elif choice == 's':
            pass
            
        else:
            print("That's not a valid choice")
            self.user_turn(other)
            
    
    def level_up(self, other): #checks if player has leveled up
                                #get monster.exp after winning duel 
        if self.exp >= self.exp_count:
            self.exp = (monster.exp + self.exp) - self.exp_count
            self.level += 1
            self.exp_count += 10
            return self.exp_count
            return self.exp, self.level
            #call function that changes stats based on level
            
    def state_change(self):
        pass
        




    def __init__(self):  #  creates character
        self.name = input("Name: ").title()
        print("Welcome {}, lets pick your attributes".format(self.name))
        self.weapon = self.get_weapon()
        print ("You chose the {}".format(self.weapon))
        
    def __str__(self):  #  prints character statistics 
            return "{} LVL: {} HP: {}/{} XP: {}/{} Gold: {}".format(self.name, self.level, self.current_hp, self.base_hp, self.exp,                                                              self.exp_count, self.gold) # bad syntax

        


    
def get_monster(): #loads opponent to screen for player to face 

    
    if player.level < 3:
        opponent = Grunt()
        
        return opponent
        
    elif player.level < 7:
        coin_flip = random.randint(1,2)
        
        if coin_flip == 1:
            opponent = Grunt()
            return opponent
        else:
            opponent = Goblin()
            return opponent
            
    elif player.level < 10:
        coin_flip = random.randint(1,4)
        if coin_flip == 1:
            opponent = Grunt()
            return opponent
            
        elif coin_flip == 2 or coin_flip == 3:
            opponent = Goblin()
            return opponent
            
        else:
            opponent = Ogre()
            return opponent
            
    elif player.level < 13:
        coin_flip = random.randint(1,6)
        if coin_flip == 1:
            opponent = Grunt()
            return opponent
        elif coin_flip == 2 or coin_flip == 3:
            opponent = Goblin()
            return opponent
        elif coin_flip == 4 or coin_flip == 5:
            opponent = Ogre()
            return opponent
        else:
            opponent = DarkElf()
            return opponent
        
    elif player.level < 15:
            coin_flip = random.randint(1,8)
            if coin_flip == 1:
                opponent = Grunt()
                return opponent
            elif coin_flip == 2:
                opponent = Goblin()
                return opponent
            elif coin_flip == 3 or coin_flip == 4:
                opponent = Ogre()
                return opponent
            elif coin_flip == 5 or coin_flip == 6:
                opponent = DarkElf()
                return opponent
            else:
                opponent = Dragon()
                return opponent
        
    
player = Character()
print ('\n')
print (player)
print ('=' * 50)
monsters_defeated = 0

while player.current_hp > 0:
    
    
    monster = get_monster()
    
    if monster.suprise() == True:
        suprise_damage = monster.attack()
        player.current_hp -= suprise_damage
        print("A monster lunges at you from the darkness!")
        monster.battlecry()
    
        print("Dealing {} damage to you!".format(suprise_damage))
        
        
    else:
        print("You have encountered a monster:")
        monster.battlecry()
        
        
    while player.current_hp > 0 and monster.current_hp > 0:
        
        print(player)
        print(monster)
        
        player.user_turn(monster)
        print('\n')
        
        if monster.current_hp > 0:
            monster.monster_turn(player)    
            print('='*50)
            
        elif player.current_hp == 0:
            break
            
        elif monster.current_hp == 0:
            monsters_defeated += 1
            player.exp += monster.exp
            player.gold += monster.gold
            player.level_up(monster)
            print("You defeated the Monster")
            print('='*50)
            
            
print("Victory has defeated you")
print("You killed {} Monsters.".format(monsters_defeated))
