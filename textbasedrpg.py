import random
import copy
class Weapon:
    def __init__(self, damage, speed, name):
        self.damage = damage
        self.speed = speed
        self.name = name

class Enemy:
    def __init__(self, name, attack, weaponspeed, weaponname, health, description,weapontable):
        self.attack = attack
        self.name = name
        self.weaponname = weaponname
        self.weaponspeed = weaponspeed
        self.health = health
        self.description = description
        self.weapontable = weapontable

    def attackmanage(self, newweapon):
        self.attack = newweapon.damage
        self.weaponname = newweapon.name
        self.weaponspeed = newweapon.speed

    def Damage(self, damage):
        self.health = int(self.health) - int(damage)


class Room:
    def __init__(self, name, description,north,south,east,west,enemytable):
        self.name = name
        self.description = description
        self.north = north
        self.south = south
        self.west = west
        self.east = east
        self.enemytable = enemytable
    def roomcheck(self):
      print(self.name)
    def Move(self,newroom):
      self.name = newroom.name
      self.description = newroom.description
      self.north = newroom.north
      self.south = newroom.south
      self.west = newroom.west
      self.east = newroom.east
    def build(self,newname,newdescription,newnorth,newsouth,newwest,neweast,newenemies):
      self.name = newname
      self.description = newdescription
      self.north = newnorth
      self.south = newsouth
      self.west = newwest
      self.east = neweast
      self.enemytable = newenemies

class You:
    def __init__(self, name, attack, weaponspeed, weaponname, health):
        self.attack = attack
        self.name = name
        self.weaponname = weaponname
        self.weaponspeed = weaponspeed
        self.health = health

    def healthcheck(self):
        print("Your Health Is", self.health)

    def healthmanage(self, newhealth):
        self.health = newhealth
    def damage(self,enemyattack):
        self.health = int(self.health) - int(enemyattack)

    def attackcheck(self):
        print("Your Weapon Is", self.weaponname)
        print("Your Weapon Damage Is", self.attack)
        print("Your Weapon Speed Is", self.weaponspeed)

    def attackmanage(self, newdamage, newweaponname, newspeed):
        self.attack = newdamage
        self.weaponname = newweaponname
        self.weaponspeed = newspeed
def moveroom(OcRoom):
  movedirection = input("What direction would you like to move? ")
  if movedirection == "North":
    OcRoom.Move(OcRoom.north)
    print("You have moved to %s"% OcRoom.name)
    return(OcRoom)
  if movedirection == "South":
    OcRoom.Move(OcRoom.south)  
    print("You have moved to %s"% OcRoom.name)
    return(OcRoom)
  if movedirection == "West":
    OcRoom.Move(OcRoom.west)
    print("You have moved to %s"% OcRoom.name)
    return(OcRoom)
  if movedirection == "East":
    OcRoom.Move(OcRoom.east)
    print("You have moved to %s"% OcRoom.name)
    return(OcRoom)
def Commandline(alwaysrun,Engaged,Hero):
  while alwaysrun < 1:
    while not Engaged.name == "None":
        print("you are in combat")
        Combatcommandline(Engaged,Hero)
        Engaged = copy.deepcopy(Blankenemy)
    while Engaged.name == "None":
        print("You are not in combat")
        Maincommandline(Engaged,Hero)
def combat(Engaged,Hero):
  if int(Engaged.weaponspeed) > int(Hero.weaponspeed):
    Hero.damage(Engaged.attack)
    Engaged.Damage(Hero.attack)
  if int(Engaged.weaponspeed) < int(Hero.weaponspeed):
    Engaged.Damage(Hero.attack)
    Hero.damage(Engaged.attack)
  if int(Engaged.weaponspeed) == int(Hero.weaponspeed):
    attackfirst = random.randint(1,2)
    if attackfirst == 1:
      Engaged.Damage(Hero.attack)
      Hero.damage(Engaged.attack)
    if attackfirst == 2:
      Hero.damage(Engaged.attack)
      Engaged.Damage(Hero.attack)
def Maincommandline(Engaged,Hero):
    global maininput
    maininput = input("")
    print(Engaged.name)
    if maininput == "Healthcheck":
        You.healthcheck(Hero)
    if maininput == "Attackcheck":
        You.attackcheck(Hero)
    if maininput == "Roomcheck":
      OcRoom.roomcheck()
    if maininput == "Roomdesc":
      print(OcRoom.description)
    if maininput == "Move":
      moveroom(OcRoom)
    if maininput == "Fight":
      Engaged = copy.deepcopy(random.choice(OcRoom.enemytable))
      print(Engaged.name)
      Engaged.attackmanage(random.choice(Engaged.weapontable))
      Commandline(alwaysrun,Engaged,Hero)
def Combatcommandline(Engaged,Hero):
    Cengaged = Engaged
    while int(Cengaged.health) > 0:
        global combatinput
        combatinput = input("")
        if combatinput == "Healthcheck":
            You.healthcheck(Hero)
        if combatinput == "Attackcheck":
            You.attackcheck(Hero)
        if combatinput == "Attack":
            combat(Engaged,Hero)
            print("The enemy's health is %s"% Engaged.health)
            print("Your health is %s"% Hero.health)
            if int(Hero.health) < 0 or int(Hero.health) == 0:
              print("You have died")
              quit()
            
            
    Engaged = copy.deepcopy(Blankenemy)
global alwaysrun
alwaysrun = 0
Fist = Weapon(1, 5, "Fist")
BFist = Weapon(6,1,"Fist")
Cudgel = Weapon(10, 0.5,"Cudgel")
CDagger = Weapon(3, 4, "Common Dagger")
CSword = Weapon(5, 2, "Common Sword")
Commonweapon = [CDagger,CSword]
Bruteweapon = [BFist,Cudgel]
Blankenemy = Enemy("None",None,None,"None",None,"None",None)
Engaged = copy.deepcopy(Blankenemy)
Bandit = Enemy(
    "Bandit",
    1,
    1,
    "sometin broke",
    10,
    "A hunched figure stands by the side of the road. different mismatched clothing obscures even the barest hint of their identity",Commonweapon)
Goblin = Enemy("Goblin",1,1,"sometin broke",15,"This hulking greenish brute has four fingers and is dressed in a simple loincloth. It brings with it the smell of rot and mold",Commonweapon)
Troll = Enemy("Troll",1,1,"sometin broke",40,"This giant creature is nearly 3 times larger than you. It has shaggy fur and razorsharp ivory tusks. Its beady red eyes burn with hatred and hunger",Bruteweapon)
roadenemies = [Goblin,Bandit]
forestenemies = [Goblin,Troll]
houseenemies = [Bandit,Troll]
NullRoom = Room(None,None,None,None,None,None,None)
Road = copy.deepcopy(NullRoom)
Forest = copy.deepcopy(NullRoom)
House =  copy.deepcopy(NullRoom)
Road.build("Road","The road is made of a dry, yellowish dirt. The road is hard packed from decades of use.", House, Road,Forest,Forest,roadenemies)
House.build("House","The white paint flakes off the walls of the old house, the front door creaks open and closed with the blowing of the wind",Forest,Road,Forest,Forest,houseenemies)
Forest.build("Forest","The trees close in around you, the area is dimly lit by the few areas where the sun peaks through the canopy",Forest,Forest,Forest,Forest,forestenemies)
Eweapon = Fist
OcRoom = Road
yname = input("Hello hero. Please tell us your name")
Hero = You(yname, 0, 0, "Somethin broke", 100)
Hero.attackmanage(Eweapon.damage, Eweapon.name, Eweapon.speed)
Doublecheckname = input("Your name is %s correct?" % yname)
if Doublecheckname == "No":
    yname = input("I guess I misheard, what is your name")
if Doublecheckname == "Yes":
    print(
        "Splendid, now as you can see, we are in a bit of a pickle. There are a few goblins planning to eat us. Please take a weapon and defend the us"
    )
    chooseweapon = input(
        "I have a Common Dagger and a Common Sword, which would you like"
    )
    if chooseweapon == "Common Dagger":
        Eweapon = CDagger
        Hero.attackmanage(Eweapon.damage, Eweapon.name, Eweapon.speed)
    if chooseweapon == "Common Sword":
        Eweapon = CSword
        Hero.attackmanage(Eweapon.damage, Eweapon.name, Eweapon.speed)
    print("Now Fight")
    Engaged = copy.deepcopy(Goblin)
Commandline(alwaysrun,Engaged,Hero)

