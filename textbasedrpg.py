class Weapon:
    def __init__(self, damage, speed, name):
        self.damage = damage
        self.speed = speed
        self.name = name


class Enemy:
    def __init__(self, name, attack, weaponspeed, weaponname, health, description):
        self.attack = attack
        self.name = name
        self.weaponname = weaponname
        self.weaponspeed = weaponspeed
        self.health = health
        self.description = description

    def attackmanage(self, newdamage, newweaponname, newspeed):
        self.attack = newdamage
        self.weaponname = newweaponname
        self.weaponspeed = newspeed

    def Damage(self, damage):
        self.health = int(self.health) - int(damage)


class Room:
    def __init__(self, name, description):
        self.name = name
        self.description = description


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

    def attackcheck(self):
        print("Your Weapon Is", self.weaponname)
        print("Your Weapon Damage Is", self.attack)
        print("Your Weapon Speed Is", self.weaponspeed)

    def attackmanage(self, newdamage, newweaponname, newspeed):
        self.attack = newdamage
        self.weaponname = newweaponname
        self.weaponspeed = newspeed


def Maincommandline():
    global maininput
    maininput = input("")
    if maininput == "Healthcheck":
        You.healthcheck(Hero)
    if maininput == "Attackcheck":
        You.attackcheck(Hero)


def Combatcommandline(Engaged):
    Cengaged = Engaged
    while int(Cengaged.health) > 0:
        global combatinput
        combatinput = input("")
        if combatinput == "Healthcheck":
            You.healthcheck(Hero)
        if combatinput == "Attackcheck":
            You.attackcheck(Hero)
        if combatinput == "Attack":
            Engaged.Damage(Hero.attack)
            print(Engaged.health)


Engaged = None
Goblin = Enemy(
    "Goblin",
    0,
    0,
    "sometin broke",
    15,
    "This hulking greenish brute has four fingers and is dressed in a simple loincloth. It brings with it the smell of rot and mold",
)
Road = Room(
    "Road",
    "The road is made of a dry, yellowish dirt. The road is hard packed from decades of use.",
)
Fist = Weapon(1, 5, "Fist")
CDagger = Weapon(3, 4, "Common Dagger")
CSword = Weapon(5, 2, "Common Sword")
Eweapon = Fist
yname = input("Hello hero. Please tell us your name")
Hero = You(yname, 0, 0, "Somethin broke", 100)
Hero.attackmanage(Eweapon.damage, Eweapon.name, Eweapon.speed)
Doublecheckname = input("Your name is %s correct?" % yname)
if Doublecheckname == "No":
    yname = input("I guess I misheard, what is your name")
if Doublecheckname == "Yes":
    print(
        "Splendid, now as you can see, we are in a bit of a pickle. There are a few goblins planning to eat us. Please take a weapon and defend the village"
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
    Engaged = Goblin
while Engaged == None:
    Maincommandline()
while not Engaged == None:
    print("you are in combat")
    Combatcommandline(Engaged)
