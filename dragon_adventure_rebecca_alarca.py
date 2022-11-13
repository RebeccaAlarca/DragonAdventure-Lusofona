
import sys
import os
import random

# efeitos de texto (letra)
reset = '\033[0m'
bold = '\033[01m'
underline = '\033[04m'
# efeitos de texto(cor da letra)
darkgrey = '\033[90m'
red = '\033[31m'
lightcyan = '\033[96m'
green = '\033[32m'
#efeitos de cor(fundo)
lightgrey_bg = '\033[47m'

# função para manter as cores
def base():
	return(print(reset + lightgrey_bg + darkgrey))

# características dos personagens
class Warrior:
#construtor da classe
    def __init__(self,name):
        self.name = name
        self.HP = 32
        self.MP = 5
        self.AP = 2
        self.WP = 5
        self.INIT = 2
#métodos spell
    def spellEffect_W(self):
        return self.WP + warrior.rollDice(4)
    
# custo do spell
    def spellCost(self):
        self.MP =- 5
        if self.MP <= 0:
            self.MP = 0
        return 0
        
    def wcanSpell(self):  # condição para saber se warrior pode ou não lançar o spell
        cost = self.spellCost()
        if cost <= self.MP:
            return True
        if cost > self.MP:
            print(" You don't have enough MP to use this spell.")
            return False

    def rollDice(self,faces): # para os dados d4, d6 e d20
        return random.randint(1,faces)
warrior = Warrior("Warrior")

class Priest:
    def __init__(self,name):
            self.name = name
            self.HP = 20
            self.MP = 25
            self.AP = 0
            self.WP = 4
            self.INIT = 6

    def spellEffect_P(self,effect):
        if effect == 1:
            return priest.rollDice(4) * 2
        if effect == 2:
            return priest.rollDice(6) + self.WP
    
# custo do spell
    def spellCostP(self,effect):
        if effect == 1:
            self.MP -= 5
            if self.MP <= 0:
                self.MP = 0
        if effect == 2:
            self.MP -= 3
            if self.MP <= 0:
                self.MP = 0
        return 0
    def pcanSpell(self, effect):
        cost = self.spellCostP(effect)
        if cost <= self.MP:
            return True
        elif cost > self.MP:
            print(" You don't have enough MP to use this spell.")
            return False
    def rollDice(self,faces):
        return random.randint(1,faces)
priest = Priest("Priest")

#### Inimigos 
class Enemy1:
    def __init__(self,name):
        self.name = name
        self.HP = 15
        self.AP = 2
        self.WP = 3
        self.INIT = 2
    def rollDice(self,faces):
        return random.randint(1,faces)
Orc1 = Enemy1("Orc Warrior 1")
class Enemy2:
    def __init__(self,name):
        self.name = name
        self.HP = 15
        self.AP = 2
        self.WP = 3
        self.INIT = 2
Orc2 = Enemy2("Orc Warrior 2")
class Enemy3:
    def __init__(self,name):
        self.name = name
        self.HP = 15
        self.AP = 2
        self.WP = 3
        self.INIT = 2
Orc3 = Enemy3("Orc Warrior 3")
class Enemy4:
    def __init__(self,name):
        self.name = name
        self.HP = 15
        self.AP = 2
        self.WP = 3
        self.INIT = 2
Orc4 = Enemy4("Orc Warrior 4")           

#lista pra tirar personagens do jogo caso morram (será usado nas funçoes fight() e otherRound())
stillalive = ["warrior","priest","Orc1","Orc2","Orc3","Orc4"]


## INTRO ##
def start():
    print(bold + " Welcome to the Dragon Adventure World, warrior!"), base()
    print(" You are in the middle of a battle, so you must be careful. But," + bold + " DON'T PANIC!")
    base()
    print(' You are not alone.\n Know your team:\n ')
    print(bold + "  WARRIOR")
    base()
    print(" HP: 32 \n MP: 5 \n AP: 2 \n WP: 5 \n Init: 2 \n " + underline + bold + "\n Spells: \n Rushdown (Apply on Enemy)"), base()
    print(" > Effect: -1 * (WP + d4) \n > Cost: 5MP \n" )
    print(bold + "  PRIEST")
    base()
    print(" HP: 20 \n MP: 25 \n AP: 0 \n WP: 2 \n Init: 6 \n" + underline + bold + "\n Spells: \n Exorcism (Apply on Enemy) "), base()
    print(" > Effect:-1 * (d4 * 2) \n > Cost: 5MP \n" + underline + bold + " \n Mend (Apply on Ally) "), base()
    print(" > Effect: d6 + WP \n > Cost: 3MP \n")
    print(" Also, get to know your enemies: they are 4 and all of them have the same attributes.")
    print(bold + "  ORC WARRIORS")
    base()
    print(" HP: 15 \n MP: 0 \n AP: 2 \n WP: 3 \n Init: 2 \n")

    # se precisa de mais detalhes
    linfo = True
    while linfo:
        info = str(input("\n > Do you need more info about HP, MP, AP, WP and Init?(Y/N) > "))
    
        if info.upper() == "Y":
            linfo = False
            print(" Hit-Points (HP): It represents how much of life the character still has, until it dies.")
            print(" Mana-Points (MP): If you want to cast spells, they are not free. This represents how much can you spend for the spells.")
            print(" Armor Points (AP): We all have our defenses. It will subtract from the damage you or the enemy had.")
            print(" Weapon (WP): How much damage the character is able to do.")
            print(" Initiative (Init): The bigger the number, the fastest the Initiative. If d20 allows.")
            pass
        elif info.upper() == "N":
            print(" Great! So let's get started! \n")
            linfo = False
        else:
            print("Please, press Y or N.")

## MENU 
base()
def menu():
    os.system('cls')
    print(bold + " DRAGON ADVENTURE \n")
    base()
    print("1. START GAME")
    print("2. EXIT")
    option = input("> ")
    if option == "1":
        start()
    elif option == "2":
        sys.exit()
    else:
        menu()
menu()

def whoinit(): # FASE INICIAÇÃO turnOrder pra ver quem começa > turnOrder = d20 + init
    roll = str(input(bold +"\n Hands Up, everyone. Roll the dice and see who's first. (write roll) > "))
    base()
    if roll:
        global turnOrder
        global name
        allinit = {"Warrior":warrior.INIT,"Priest":priest.INIT,"Orc1":Orc1.INIT} # dicionário para todos os Init. Só o primeiro inimigo pois todos tem os mesmos valores
        allinit ["Warrior"] += warrior.rollDice(20)
        allinit ["Priest"] += priest.rollDice(20)
        allinit ["Orc1"] += Orc1.rollDice(20)
        turnOrder = 0
        name = ""
        if allinit["Warrior"] > allinit["Priest"] and allinit["Warrior"] > allinit["Orc1"]:
            turnOrder = allinit["Warrior"]
            name = "Warrior"

        elif allinit["Priest"] > allinit["Warrior"] and allinit["Priest"] > allinit["Orc1"]:
            turnOrder = allinit["Priest"]
            name = "Priest"
        else:
            turnOrder = allinit["Orc1"]
            name = "Orc1"
        print(" Warrior rolled the d20 + it's INIT > " + str(allinit["Warrior"]))
        print(" Priest rolled the d20 + it's INIT > " + str(allinit["Priest"]))
        print(" Orc1 rolled the d20 + it's INIT > " + str(allinit["Orc1"]))
        print(" " + bold + name + " is the starter, with " + str(turnOrder) + " in the roll.")
        base()
whoinit()

## FASE DE AÇÃO INICIAL 
def fight(name):
    print(" ")
    if name == "Warrior":
        print(" Choose if you want to use a spell or attack.")
        option = input(" 1.Spell \n 2.Attack > ")
        if option == "1":
            if warrior.wcanSpell(): # implementação da função para avançar ou não no spell
                print(red + " Warrior now has " + str(warrior.MP) + " MP.")
                base()
            else:
                print (" You don't have enough MP to use this spell.")
                option = input(" 1.Spell \n 2.Attack > ")

            print(" Choose who do you want to attack: ") # escolher inimigos para usar o spell
            enemies = input(" 1. Orc Warrior 1 \n 2. Orc Warrior 2 \n 3. Orc Warrior 3 \n 4. Orc Warrior 4 > ")
            if enemies == "1":
                if "Orc1" in stillalive:
                    Orc1.HP -= warrior.spellEffect_W()
                    print(" Warrior hit " + str(warrior.spellEffect_W()) + " points of damage.")
                    if Orc1.HP > 0:
                        print(bold+ red +" Orc Warrior 1 now has " + str(Orc1.HP) + " HP.")
                        base()
                    if Orc1.HP <= 0:
                        Orc1.HP = 0
                        print(bold + red + " Orc Warrior 1 is DEAD.")
                        base()
                        stillalive.remove("Orc1")
                    
            elif enemies == "2":
                if "Orc2" in stillalive:
                    Orc2.HP -= warrior.spellEffect_W()
                    print(" Warrior hit " + str(warrior.spellEffect_W()) + " points of damage.")
                    if Orc2.HP > 0:
                        print(bold+ red +" Orc Warrior 2 now has " + str(Orc2.HP) + " HP.")
                        base()
                    if Orc2.HP <= 0:
                        Orc2.HP = 0
                        print(bold + red + " Orc Warrior 2 is DEAD.")
                        base()
                        stillalive.remove("Orc2")

            elif enemies == "3":
                if "Orc3" in stillalive:
                    Orc3.HP -= warrior.spellEffect_W()
                    print(" Warrior hit " + str(warrior.spellEffect_W()) + " points of damage.")
                    if Orc3.HP > 0:
                        print(bold+ red +" Orc Warrior 3 now has " + str(Orc3.HP) + " HP.")
                        base()
                    if Orc3.HP <= 0:
                        Orc3.HP = 0
                        print(bold + red +" Orc Warrior 3 is DEAD.")
                        base()
                        stillalive.remove("Orc3")

            elif enemies == "4":
                if "Orc4" in stillalive:
                    Orc4.HP -= warrior.spellEffect_W()
                    print(" Warrior hit " + str(warrior.spellEffect_W()) + " points of damage.") #
                    if Orc4.HP > 0:
                        print(bold+ red +" Orc Warrior 4 now has " + str(Orc4.HP) + " HP.")
                        base()
                    if Orc4.HP <= 0:
                        Orc4.HP = 0
                        print(bold + red + " Orc Warrior 4 is DEAD.")
                        base()
                        stillalive.remove("Orc4")


        elif option == "2": # escolha de ataque, qual inimigo 
            print(" Choose who do you want to attack: ")
            enemies = input(" 1. Orc Warrior 1 \n 2. Orc Warrior 2 \n 3. Orc Warrior 3 \n 4. Orc Warrior 4 > ")
            dmg = 0
            if enemies == "1":
                if "Orc1" in stillalive:
                    dmg = warrior.WP - Orc1.AP
                    print(" Warrior hit " + str(dmg) + " points of damage.")
                    if dmg < 0:
                        dmg = 0
                    Orc1.HP -= dmg
                    if Orc1.HP > 0:
                        print(bold + red +" Orc Warrior 1 now has " + str(Orc1.HP) + " HP.")
                        base()
                    if Orc1.HP <= 0:
                        Orc1.HP = 0
                        print(bold + red + " Orc Warrior 1 is DEAD.")
                        base()
                        stillalive.remove("Orc1")

            elif enemies == "2":
                if "Orc2" in stillalive:
                    dmg = warrior.WP - Orc2.AP
                    print(" Warrior hit " + str(dmg) + " points of damage.")
                    if dmg < 0:
                        dmg = 0
                    Orc2.HP -= dmg
                    if Orc2.HP > 0:
                        print(bold + red +" Orc Warrior 2 now has " + str(Orc2.HP) + " HP.")
                        base()
                    if Orc2.HP <= 0:
                        Orc2.HP = 0
                        print(bold + red +" Orc Warrior 2 is DEAD.")
                        base()
                        stillalive.remove("Orc2")
            elif enemies == "3":
                if "Orc3" in stillalive:
                    dmg = warrior.WP - Orc3.AP
                    print(" Warrior hit " + str(dmg) + " points of damage.")
                    if dmg < 0:
                        dmg = 0
                    Orc3.HP -= dmg
                    if Orc3.HP > 0:
                        print(bold + red +" Orc Warrior 3 now has " + str(Orc3.HP) + " HP.")
                        base()
                    if Orc3.HP <= 0:
                        Orc3.HP = 0
                        print(bold + red +" Orc Warrior 3 is DEAD.")
                        base()
                        stillalive.remove("Orc3")
            elif enemies == "4":
                if "Orc4" in stillalive:
                    dmg = warrior.WP - Orc4.AP
                    print(" Warrior hit " + str(dmg) + " points of damage.")
                    if dmg < 0:
                        dmg = 0
                    Orc4.HP -= dmg
                    if Orc4.HP > 0:
                        print(bold + red +" Orc Warrior 4 now has " + str(Orc4.HP) + " HP.")
                        base()
                    if Orc4.HP <= 0:
                        Orc4.HP = 0
                        print(bold + red +" Orc Warrior 4 is DEAD.")
                        base()
                        stillalive.remove("Orc4")
                
    ########################## PRIEST ###
    if name == "Priest":
        # escolher ataque ou spell
        print(" Choose if you want to use a spell or attack.")
        option = input(" 1. Spell \n  2. Attack > ")
        if option == "1":
            # escolher entre os 2 spells do padre
            print(" Choose your spell:")
            whichspell = input(" 1. Exorcism (Apply on Enemy - cost: 5MP)\n 2. Mend (Apply on Ally - cost: 3MP) > ")
            if whichspell == "1":
                if priest.pcanSpell(1):
                    print(bold + red +" Priest now has " + str(priest.MP) + " MP.")
                    base()
                else:
                    option = input("1. Spell \n  2. Attack > ")
                # spell 1 afeta os inimigos
                print(" Choose who do you want to attack: ")
                enemies = input(" 1. Orc Warrior 1 \n 2. Orc Warrior 2 \n 3. Orc Warrior 3 \n 4. Orc Warrior 4 > ")
                if enemies == "1":
                    if "Orc1" in stillalive:
                        Orc1.HP -= priest.spellEffect_P(1)
                        print(" Priest hit " + str(priest.spellEffect_P(1)) + " points of damage.")
                        if Orc1.HP > 0:
                            print(bold + red +" Orc Warrior 1 now has " + str(Orc1.HP) + " HP.")
                            base()
                        if Orc1.HP <= 0:
                            Orc1.HP = 0
                            print(bold + red +" Orc Warrior 1 is DEAD.")
                            base()
                            stillalive.remove("Orc1")
                elif enemies == "2":
                    if "Orc2" in stillalive:
                        Orc2.HP -= priest.spellEffect_P(1)
                        print(" Priest hit " + str(priest.spellEffect_P(1)) + " points of damage.")
                        if Orc2.HP > 0:
                            print(bold + red +" Orc Warrior 2 now has " + str(Orc2.HP) + " HP.")
                            base()
                        if Orc2.HP <= 0:
                            Orc2.HP = 0
                            print(bold + red + " Orc Warrior 2 is DEAD.")
                            base()
                            stillalive.remove("Orc2")
                elif enemies == "3":
                    if "Orc3" in stillalive:
                        Orc3.HP -= priest.spellEffect_P(1)
                        print(" Priest hit " + str(priest.spellEffect_P(1)) + " points of damage.")
                        if Orc3.HP > 0:
                            print(bold + red+" Orc Warrior 3 now has " + str(Orc3.HP) + " HP.")
                            base()
                        if Orc3.HP <= 0:
                            Orc3.HP = 0
                            print(bold + red +" Orc Warrior 3 is DEAD.")
                            base()
                            stillalive.remove("Orc3")
                elif enemies == "4":
                    if "Orc4" in stillalive:
                        Orc4.HP -= priest.spellEffect_P(1)
                        print(" Priest hit " + str(priest.spellEffect_P(1)) + " points of damage.")
                        if Orc4.HP > 0:
                            print(bold +red +" Orc Warrior 4 now has " + str(Orc4.HP) + " HP.")
                            base()
                        if Orc4.HP <= 0:
                            Orc4.HP = 0
                            print(bold + red +" Orc Warrior 4 is DEAD.")
                            base()
                            stillalive.remove("Orc4")
            if whichspell == "2":
                if priest.pcanSpell(2):    
                    print(bold + red +" Priest now has " + str(priest.MP) + " MP.")  
                # spell 2 ajuda um personagem jogável
                print(" Choose who do you want to help: ")
                ally = input(" 1.Warrior\n  2.Priest > ")
                if ally == "1":
                    warrior.HP += priest.spellEffect_P(2)
                    print(bold + lightcyan +" Priest hit " + str(priest.spellEffect_P(2)) + " points of recover.")
                    base()
                    # para nâo aumentar a vida máxima dos personagens
                    if warrior.HP > 32:
                        warrior.HP = 32
                    print(bold+ lightcyan +" Warrior now has " + str(warrior.HP) + " HP.")
                    base()
                elif ally == "2":
                    priest.HP += priest.spellEffect_P(2)
                    print(bold + lightcyan + " Priest hit " + str(priest.spellEffect_P(2)) + " points of recover.")
                    base()
                    if priest.HP > 20:
                        priest.HP = 20
                    print(bold+ lightcyan +" Priest now has " + str(priest.HP) + " HP.")
                    base()
        elif option == "2":
            print(" Choose who do you want to attack: ")
            enemies = input(" 1. Orc Warrior 1 \n 2. Orc Warrior 2 \n 3. Orc Warrior 3 \n 4. Orc Warrior 4 > ")
            dmg = 0
            if enemies == "1":
                if "Orc1" in stillalive:
                    dmg = priest.WP - Orc1.AP
                    print(" Priest hit " + str(dmg) + " points of damage.")
                    if dmg < 0:
                        dmg = 0
                    Orc1.HP -= dmg
                    if Orc1.HP > 0:
                        print(bold+red +" Orc Warrior 1 now has " + str(Orc1.HP) + " HP.")
                        base()
                    if Orc1.HP <= 0:
                            Orc1.HP = 0
                            print(bold + red + " Orc Warrior 1 is DEAD.")
                            base()
                            stillalive.remove("Orc1")
            elif enemies == "2":
                if "Orc2" in stillalive:
                    dmg = priest.WP - Orc2.AP
                    print(" Priest hit " + str(dmg) + " points of damage.")
                    if dmg < 0:
                        dmg = 0
                    Orc2.HP -= dmg
                    if Orc2.HP > 0:
                        print(bold+red +" Orc Warrior 2 now has " + str(Orc2.HP) + " HP.")
                        base()
                    if Orc2.HP <= 0:
                            Orc2.HP = 0
                            print(bold + red +" Orc Warrior 2 is DEAD.")
                            base()
                            stillalive.remove("Orc2")
            elif enemies == "3":
                if "Orc3" in stillalive:
                    dmg = priest.WP - Orc3.AP
                    print(" Priest hit " + str(dmg) + " points of damage.")
                    if dmg < 0:
                        dmg = 0
                    Orc3.HP -= dmg
                    if Orc3.HP > 0:
                        print(bold +red +" Orc Warrior 3 now has " + str(Orc3.HP) + " HP.")
                        base()
                    if Orc3.HP <= 0:
                            Orc3.HP = 0
                            print(bold + red +" Orc Warrior 3 is DEAD.")
                            base()
                            stillalive.remove("Orc3")
            elif enemies == "4":
                if "Orc4" in stillalive:
                    dmg = priest.WP - Orc4.AP
                    print(" Priest hit " + str(dmg) + " points of damage.")
                    if dmg < 0:
                        dmg = 0
                    Orc4.HP -= dmg
                    if Orc4.HP > 0:
                        print(bold + red +" Orc Warrior 4 now has " + str(Orc4.HP) + " HP.")
                        base()
                    if Orc4.HP <= 0:
                            Orc4.HP = 0
                            print(bold + red +" Orc Warrior 4 is DEAD.")
                            base()
                            stillalive.remove("Orc4")
############################## INIMIGO ###
    if name == "Orc1":
        attacksomeone = random.randint(1,2)
        print(" Orc Warrior 1 comes in your direction full of rage!")
        if attacksomeone == 1:
            if "warrior" in stillalive:
                print(" He attacks your Warrior and has no mercy.")
                dmg = Orc1.WP - warrior.AP
                print(" Orc 1 hit " + str(dmg) + " points of damage.")
                if dmg < 0:
                    dmg = 0
                warrior.HP -= dmg
                if warrior.HP > 0:
                    print(bold + red +" Warrior now has " + str(warrior.HP) + " HP.")
                    base()
                if warrior.HP <= 0:
                    print(bold+ red +" Warrior is DEAD.")
                    base()
                    stillalive.remove("warrior")
            else:
                attacksomeone == [1]
        if attacksomeone == 2:
            if "priest" in stillalive:
                print(" He attacks your Priest and has no mercy.")
                dmg = Orc1.WP - priest.AP
                print(" Orc 1 hit " + str(dmg) + " points of damage.")
                if dmg < 0:
                    dmg = 0
                priest.HP -= dmg
                if priest.HP > 0:
                    print(bold + red+ " Priest now has " + str(priest.HP) + " HP.")
                    base()
                if priest.HP <= 0:
                    print(bold+red + " Priest is DEAD.")
                    base()
                    stillalive.remove("priest")
            else:
                attacksomeone == [0]
        
  
############################## rounds em ciclo
def otherRound():
    
    ret = True
    while ret:
        print(" ")
        fight(name)
        def warriorFight(): # Função para toda vez que o WARRIOR jogar.
            if "warrior" in stillalive:
                print(bold + " It's Warrior's turn! ")
                base()
                print(" Choose if you want to use a spell or attack.")
                option = input(" 1.Spell \n  2.Attack > ")
                if option == "1":
                    if warrior.wcanSpell():
                        print(bold + red +" Warrior now has " + str(warrior.MP) + " MP.")
                        base()
                    else:
                        print (underline + red +" You don't have enough MP to use this spell.")
                        base()
                        option = input("1. Spell \n 2.Attack > ")

                    print(" Choose who do you want to attack: ") # escolher alguém para atacar
                    enemies = input(" 1. Orc Warrior 1 \n 2. Orc Warrior 2 \n 3. Orc Warrior 3 \n 4. Orc Warrior 4 > ")
                    if enemies == "1":
                        if "Orc1" in stillalive:
                            Orc1.HP -= warrior.spellEffect_W()
                            print(" Warrior hit " + str(warrior.spellEffect_W()) + " points of damage.")
                            if Orc1.HP > 0:
                                print(bold+red+" Orc Warrior 1 now has " + str(Orc1.HP) + " HP.")
                                base()
                            if Orc1.HP <= 0:
                                Orc1.HP = 0
                                print(bold + red +" Orc Warrior 1 is DEAD.")
                                base()
                                stillalive.remove("Orc1")
                            
                    elif enemies == "2":
                        if "Orc2" in stillalive:
                            Orc2.HP -= warrior.spellEffect_W()
                            print(" Warrior hit " + str(warrior.spellEffect_W()) + " points of damage.")
                            if Orc2.HP > 0:
                                print(bold+red +" Orc Warrior 2 now has " + str(Orc2.HP) + " HP.")
                                base()
                            if Orc2.HP <= 0:
                                Orc2.HP = 0
                                print(bold + red +" Orc Warrior 2 is DEAD.")
                                base()
                                stillalive.remove("Orc2")

                    elif enemies == "3":
                        if "Orc3" in stillalive:
                            Orc3.HP -= warrior.spellEffect_W()
                            print(" Warrior hit " + str(warrior.spellEffect_W()) + " points of damage.")
                            if Orc3.HP > 0:
                                print(bold+red+" Orc Warrior 3 now has " + str(Orc3.HP) + " HP.")
                                base()
                            if Orc3.HP <= 0:
                                Orc3.HP = 0
                                print(bold + red +" Orc Warrior 3 is DEAD.")
                                base()
                                stillalive.remove("Orc3")

                    elif enemies == "4":
                        if "Orc4" in stillalive:
                            Orc4.HP -= warrior.spellEffect_W()
                            print(" Warrior hit " + str(warrior.spellEffect_W()) + " points of damage.") #
                            if Orc4.HP > 0:
                                print(bold+red +" Orc Warrior 4 now has " + str(Orc4.HP) + " HP.")
                                base()
                            if Orc4.HP <= 0:
                                Orc4.HP = 0
                                print(bold + red +" Orc Warrior 4 is DEAD.")
                                base()
                                stillalive.remove("Orc4")

                elif option == "2":
                    print(" Choose who do you want to attack: ")
                    enemies = input(" 1. Orc Warrior 1 \n 2. Orc Warrior 2 \n 3. Orc Warrior 3 \n 4. Orc Warrior 4 > ")
                    dmg = 0
                    if enemies == "1":
                        if "Orc1" in stillalive:
                            dmg = warrior.WP - Orc1.AP
                            print(" Warrior hit " + str(dmg) + " points of damage.")
                            if dmg < 0:
                                dmg = 0
                            Orc1.HP -= dmg
                            if Orc1.HP > 0:
                                print(bold+red +" Orc Warrior 1 now has " + str(Orc1.HP) + " HP.")
                                base()
                            if Orc1.HP <= 0:
                                Orc1.HP = 0
                                print(bold + red + " Orc Warrior 1 is DEAD.")
                                base()
                                stillalive.remove("Orc1")

                    elif enemies == "2":
                        if "Orc2" in stillalive:
                            dmg = warrior.WP - Orc2.AP
                            print(" Warrior hit " + str(dmg) + " points of damage.")
                            if dmg < 0:
                                dmg = 0
                            Orc2.HP -= dmg
                            if Orc2.HP > 0:
                                print(bold+red+" Orc Warrior 2 now has " + str(Orc2.HP) + " HP.")
                                base()
                            if Orc2.HP <= 0:
                                Orc2.HP = 0
                                print(bold + red+" Orc Warrior 2 is DEAD.")
                                base()
                                stillalive.remove("Orc2")
                    elif enemies == "3":
                        if "Orc3" in stillalive:
                            dmg = warrior.WP - Orc3.AP
                            print(" Warrior hit " + str(dmg) + " points of damage.")
                            if dmg < 0:
                                dmg = 0
                            Orc3.HP -= dmg
                            if Orc3.HP > 0:
                                print(bold+red+" Orc Warrior 3 now has " + str(Orc3.HP) + " HP.")
                                base()
                            if Orc3.HP <= 0:
                                Orc3.HP = 0
                                print(bold + red + " Orc Warrior 3 is DEAD.")
                                base()
                                stillalive.remove("Orc3")
                    elif enemies == "4":
                        if "Orc4" in stillalive:
                            dmg = warrior.WP - Orc4.AP
                            print(" Warrior hit " + str(dmg) + " points of damage.")
                            if dmg < 0:
                                dmg = 0
                            Orc4.HP -= dmg
                            if Orc4.HP > 0:
                                print(bold+red +" Orc Warrior 4 now has " + str(Orc4.HP) + " HP.")
                                base()
                            if Orc4.HP <= 0:
                                Orc4.HP = 0
                                print(bold + red +" Orc Warrior 4 is DEAD.")
                                base()
                                stillalive.remove("Orc4")
                else: # se o warrior estiver morto, o controle passa para o priest.
                    priestFight()
                pass
                    
        def priestFight(): # Função para toda vez que o PRIEST jogar
            # escolher ataque ou spell
            if "priest" in stillalive:
                print(bold + "It's PRIEST'S turn!")
                base()
                print(" Choose if you want to use a spell or attack.")
                option = input(" 1. Spell \n 2.Attack > ")
                if option == "1":
                    # escolher entre os 2 spells do padre
                    print(" Choose your spell:")
                    whichspell = input(" 1. Exorcism (Apply on Enemy - cost: 5MP)\n 2. Mend (Apply on Ally - cost: 3MP) > ")
                    if whichspell == "1":
                        if priest.pcanSpell(1):
                            print(red + bold +"Priest now has " + str(priest.MP) + " MP.")
                            base()
                        if priest.MP <= 0:
                            print(red + underline+"You don't have enough MP to use this spell")
                            base()
                            option = input("1. Spell \n 2.Attack > ")
                        # spell 1 afeta os inimigos
                        print(" Choose who do you want to attack: ")
                        enemies = input(" 1. Orc Warrior 1 \n 2. Orc Warrior 2 \n 3. Orc Warrior 3 \n 4. Orc Warrior 4 > ")
                        if enemies == "1":
                            if "Orc1" in stillalive:
                                Orc1.HP -= priest.spellEffect_P(1)
                                print(" Priest hit " + str(priest.spellEffect_P(1)) + " points of damage.")
                                if Orc1.HP > 0:
                                    print(bold+red +" Orc Warrior 1 now has " + str(Orc1.HP) + " HP.")
                                    base()
                                if Orc1.HP <= 0:
                                    Orc1.HP = 0
                                    print(bold + red +" Orc Warrior 1 is DEAD.")
                                    base()
                                    stillalive.remove("Orc1")
                        elif enemies == "2":
                            if "Orc2" in stillalive:
                                Orc2.HP -= priest.spellEffect_P(1)
                                print(" Priest hit " + str(priest.spellEffect_P(1)) + " points of damage.")
                                if Orc2.HP > 0:
                                    print(bold+red+" Orc Warrior 2 now has " + str(Orc2.HP) + " HP.")
                                    base()
                                if Orc2.HP <= 0:
                                    Orc2.HP = 0
                                    print(bold + red +" Orc Warrior 2 is DEAD.")
                                    base()
                                    stillalive.remove("Orc2")
                        elif enemies == "3":
                            if "Orc3" in stillalive:
                                Orc3.HP -= priest.spellEffect_P(1)
                                print(" Priest hit " + str(priest.spellEffect_P(1)) + " points of damage.")
                                if Orc3.HP > 0:
                                    print(bold+red+" Orc Warrior 3 now has " + str(Orc3.HP) + " HP.")
                                    base()
                                if Orc3.HP <= 0:
                                    Orc3.HP = 0
                                    print(bold + red +" Orc Warrior 3 is DEAD.")
                                    base()
                                    stillalive.remove("Orc3")
                        elif enemies == "4":
                            if "Orc4" in stillalive:
                                Orc4.HP -= priest.spellEffect_P(1)
                                print(" Priest hit " + str(priest.spellEffect_P(1)) + " points of damage.")
                                if Orc4.HP > 0:
                                    print(bold +red +" Orc Warrior 4 now has " + str(Orc4.HP) + " HP.")
                                    base()
                                if Orc4.HP <= 0:
                                    Orc4.HP = 0
                                    print(bold + red +" Orc Warrior 4 is DEAD.")
                                    base()
                                    stillalive.remove("Orc4")
                    if whichspell == "2":
                        if priest.pcanSpell(2):    
                            print(red + bold +"Priest now has " + str(priest.MP) + " MP.")  
                            base()
                        if priest.MP <= 0:
                            print(red + underline+"You don't have enough MP to use this spell")
                            base()
                            option = input("1. Spell \n 2.Attack > ")

                        # spell 2 ajuda um personagem jogável
                        print(" Choose who do you want to help: ")
                        ally = input(" 1.Warrior\n 2.Priest > ")
                        if ally == "1":
                            warrior.HP += priest.spellEffect_P(2)
                            print(bold + lightcyan +" Priest hit " + str(priest.spellEffect_P(2)) + " points of recover.")
                            base()
                            # para nâo aumentar a vida máxima dos personagens
                            if warrior.HP > 32:
                                warrior.HP = 32
                            print(bold+lightcyan +" Warrior now has " + str(warrior.HP) + " HP.")
                            base()
                        elif ally == "2":
                            priest.HP += priest.spellEffect_P(2)
                            print(bold + lightcyan +" Priest hit " + str(priest.spellEffect_P(2)) + " points of recover.")
                            base()
                            if priest.HP > 20:
                                priest.HP = 20
                            print(bold+ lightcyan +" Priest now has " + str(priest.HP) + " HP.")
                            base()
                elif option == "2":
                    print(" Choose who do you want to attack: ")
                    enemies = input(" 1. Orc Warrior 1 \n 2. Orc Warrior 2 \n 3. Orc Warrior 3 \n 4. Orc Warrior 4 > ")
                    dmg = 0
                    if enemies == "1":
                        if "Orc1" in stillalive:
                            dmg = priest.WP - Orc1.AP
                            print(" Priest hit " + str(dmg) + " points of damage.")
                            if dmg < 0:
                                dmg = 0
                            Orc1.HP -= dmg
                            if Orc1.HP > 0:
                                print(bold+ red +" Orc Warrior 1 now has " + str(Orc1.HP) + " HP.")
                                base()
                            if Orc1.HP <= 0:
                                    Orc1.HP = 0
                                    print(bold + red +" Orc Warrior 1 is DEAD.")
                                    base()
                                    stillalive.remove("Orc1")
                    elif enemies == "2":
                        if "Orc2" in stillalive:
                            dmg = priest.WP - Orc2.AP
                            print(" Priest hit " + str(dmg) + " points of damage.")
                            if dmg < 0:
                                dmg = 0
                            Orc2.HP -= dmg
                            if Orc2.HP > 0:
                                print(bold+red +" Orc Warrior 2 now has " + str(Orc2.HP) + " HP.")
                                base()
                            if Orc2.HP <= 0:
                                    Orc2.HP = 0
                                    print(bold + red +" Orc Warrior 2 is DEAD.")
                                    base()
                                    stillalive.remove("Orc2")
                    elif enemies == "3":
                        if "Orc3" in stillalive:
                            dmg = priest.WP - Orc3.AP
                            print(" Priest hit " + str(dmg) + " points of damage.")
                            if dmg < 0:
                                dmg = 0
                            Orc3.HP -= dmg
                            if Orc3.HP > 0:
                                print(bold +red +" Orc Warrior 3 now has " + str(Orc3.HP) + " HP.")
                                base()
                            if Orc3.HP <= 0:
                                    Orc3.HP = 0
                                    print(bold + red + " Orc Warrior 3 is DEAD.")
                                    base()
                                    stillalive.remove("Orc3")
                    elif enemies == "4":
                        if "Orc4" in stillalive:
                            dmg = priest.WP - Orc4.AP
                            print(" Priest hit " + str(dmg) + " points of damage.")
                            if dmg < 0:
                                dmg = 0
                            Orc4.HP -= dmg
                            if Orc4.HP > 0:
                                print(bold +red +" Orc Warrior 4 now has " + str(Orc4.HP) + " HP.")
                                base()
                            if Orc4.HP <= 0:
                                    Orc4.HP = 0
                                    print(bold + red +" Orc Warrior 4 is DEAD.")
                                    base()
                                    stillalive.remove("Orc4")
                else:
                    warriorFight()
                pass
   
        def Orc1Fight(): # Função para toda vez que o Orc 1 jogar
            if "Orc1" in stillalive:
                print(bold + " It's Orc's 1 turn! ")
                base()
                attacksomeone = random.randint(1,2)
                print(" Orc Warrior 1 comes in your direction full of rage!")
                if attacksomeone == 1:
                    if "warrior" in stillalive:
                        print(" He attacks your Warrior and has no mercy.")
                        dmg = Orc1.WP - warrior.AP
                        print(" Orc 1 hit " + str(dmg) + " points of damage.")
                        if dmg < 0:
                            dmg = 0
                        warrior.HP -= dmg
                        if warrior.HP > 0:
                            print(bold +red+" Warrior now has " + str(warrior.HP) + " HP.")
                            base()
                        if warrior.HP <= 0:
                            print(bold+ red+" Warrior is DEAD.")
                            base()
                            stillalive.remove("warrior")
                    else:
                        attacksomeone == 2
                if attacksomeone == 2:
                    if "priest" in stillalive:
                        print(" He attacks your Priest and has no mercy.")
                        dmg = Orc1.WP - priest.AP
                        print(" Orc 1 hit " + str(dmg) + " points of damage.")
                        if dmg < 0:
                            dmg = 0
                        priest.HP -= dmg
                        if priest.HP > 0:
                            print(bold + red +" Priest now has " + str(priest.HP) + " HP.")
                            base()
                        if priest.HP <= 0:
                            print(bold+ red+ " Priest is DEAD.")
                            base()
                            stillalive.remove("priest")
                    else:
                        attacksomeone == 1
                pass

        def Orc2Fight(): # Função para toda vez que o Orc 2 jogar
            if "Orc2" in stillalive:
                print(bold + " It's Orc's 2 turn! ")
                base()
                attacksomeone = random.randint(1,2)
                print(" Orc Warrior 2 comes in your direction full of rage!")
                if attacksomeone == 1:
                    if "warrior" in stillalive:
                        print(" He attacks your Warrior and has no mercy.")
                        dmg = Orc2.WP - warrior.AP
                        print(" Orc 2 hit " + str(dmg) + " points of damage.")
                        if dmg < 0:
                            dmg = 0
                        warrior.HP -= dmg
                        if warrior.HP > 0:
                            print(bold +red +" Warrior now has " + str(warrior.HP) + " HP.")
                            base()
                        if warrior.HP <= 0:
                            print(bold+ red +" Warrior is DEAD.")
                            base()
                            stillalive.remove("warrior")
                    else:
                        attacksomeone == [1]
                if attacksomeone == 2:
                    if "priest" in stillalive:
                        print(" He attacks your Priest and has no mercy.")
                        dmg = Orc2.WP - priest.AP
                        print(" Orc 2 hit " + str(dmg) + " points of damage.")
                        if dmg < 0:
                            dmg = 0
                        priest.HP -= dmg
                        if priest.HP > 0:
                            print(bold + red+" Priest now has " + str(priest.HP) + " HP.")
                            base()
                        if priest.HP <= 0:
                            print(bold+ red+" Priest is DEAD.")
                            base()
                            stillalive.remove("priest")
                    else:
                        attacksomeone == [0]
                pass
            
        def Orc3Fight(): # Função para toda vez que o Orc 3 jogar
            if "Orc3" in stillalive:
                print(bold + " It's Orc's 3 turn! ")
                base()
                attacksomeone = random.randint(1,2)
                print(" Orc Warrior 3 comes in your direction full of rage!")
                if attacksomeone == 1:
                    if "warrior" in stillalive:
                        print(" He attacks your Warrior and has no mercy.")
                        dmg = Orc3.WP - warrior.AP
                        print(" Orc 3 hit " + str(dmg) + " points of damage.")
                        if dmg < 0:
                            dmg = 0
                        warrior.HP -= dmg
                        if warrior.HP > 0:
                            print(bold + red+" Warrior now has " + str(warrior.HP) + " HP.")
                            base()
                        if warrior.HP <= 0:
                            print(bold+ red+" Warrior is DEAD.")
                            base()
                            stillalive.remove("warrior")
                    else:
                        attacksomeone == [1]
                if attacksomeone == 2:
                    if "priest" in stillalive:
                        print(" He attacks your Priest and has no mercy.")
                        dmg = Orc3.WP - priest.AP
                        print(" Orc 3 hit " + str(dmg) + " points of damage.")
                        if dmg < 0:
                            dmg = 0
                        priest.HP -= dmg
                        if priest.HP > 0:
                            print(bold + red +" Priest now has " + str(priest.HP) + " HP.")
                            base()
                        if priest.HP <= 0:
                            print(bold+ red+" Priest is DEAD.")
                            base()
                            stillalive.remove("priest")
                    else:
                        attacksomeone == [0]
                pass

        def Orc4Fight(): # Função para toda vez que o Orc 1 jogar
            if "Orc4" in stillalive:
                print(bold + " It's Orc's 4 turn! ")
                base()
                attacksomeone = random.randint(1,2)
                print(" Orc Warrior 4 comes in your direction full of rage!")
                if attacksomeone == 1:
                    if "warrior" in stillalive:
                        print(" He attacks your Warrior and has no mercy.")
                        dmg = Orc4.WP - warrior.AP
                        print(" Orc 4 hit " + str(dmg) + " points of damage.")
                        if dmg < 0:
                            dmg = 0
                        warrior.HP -= dmg
                        if warrior.HP > 0:
                            print(bold +red+" Warrior now has " + str(warrior.HP) + " HP.")
                            base()
                        if warrior.HP <= 0:
                            print(bold+ red+" Warrior is DEAD.")
                            base()
                            stillalive.remove("warrior")
                    else:
                        attacksomeone == 2
                if attacksomeone == 2:
                    if "priest" in stillalive:
                        print(" He attacks your Priest and has no mercy.")
                        dmg = Orc4.WP - priest.AP
                        print(" Orc 4 hit " + str(dmg) + " points of damage.")
                        if dmg < 0:
                            dmg = 0
                        priest.HP -= dmg
                        if priest.HP > 0:
                            print(bold + red +" Priest now has " + str(priest.HP) + " HP.")
                            base()
                        if priest.HP <= 0:
                            print(bold+ red +" Priest is DEAD.")
                            base()
                            stillalive.remove("priest")
                    else:
                        attacksomeone == 1
                pass
     
        
        Orc1Fight()
        priestFight()
        Orc2Fight()
        warriorFight()
        Orc3Fight()
        priestFight()
        Orc4Fight()
        
        # se os dois personagens morrerem, o jogo acaba           
        if warrior.HP <= 0 and priest.HP <= 0:
            print(bold + red + "GAME OVER")
            print(reset)
            ret = False
        # se os inimigos morrerem todos, o player ganha e o jogo acaba
        if Orc1.HP == 0 and Orc2.HP ==0 and Orc3.HP ==0 and Orc4.HP ==0:
            print(bold + green + "CONGRATULATIONS, you survived the battle!")
            base()
            wmenu = input(" 1. MENU \n  2. EXIT")
            if wmenu == "1":
                menu()
            if wmenu == "2":
                sys.exit()
            ret = False
            
    return ret

while otherRound():
    pass

print(reset)