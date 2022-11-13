import random

# efeitos de texto (letra)
reset = '\033[0m'
bold = '\033[01m'
underline = '\033[04m'
# efeitos de texto(cor da letra)
darkgrey = '\033[90m'
#efeitos de cor(fundo)
lightgrey_bg = '\033[47m'

# função para manter as cores
def base():
	return(print(reset + lightgrey_bg + darkgrey))

run = True

# características dos personagens
class Characters:
    #atributos gerais que todos os personagens tem em comum
    HP = 0
    MP = 0
    AP = 0
    WP = 0
    INIT = 0
    type = ''

#construtor da classe
    def __init__(self,HP,MP,AP,WP,INIT,type):
        self.HP = HP
        self.MP = MP
        self.AP = AP
        self.WP = WP
        self.INIT = INIT
        self.type = type

    #métodos spell
    def spellEffect_1(self,d4):
        if(self.type == 'warrior'):
            return self.WP + d4
        if(self.type == 'priest'):
            return d4 * 2
        return 0
    
    def spellEffect_2(self,d6):
        if(self.type == 'priest'):
            return d6 + self.WP
        return 0
    
    # custo do spell
    def spellCost(self,effect):
       
        if(self.type == 'warrior'):
            return self.MP - 5
        if(self.type == 'priest'):
            if effect == 1:
                return self.MP - 5
            if effect == 2:
                return self.MP - 3
        return 0

    def canSpell(self,effect):
        cost = self.spellCost(effect)  
        if cost <= self.MP:
            return True
        print(" You don't have enough MP to use this spell.")

        return False

    def rollDice(self,faces):
        return random.randint(1,faces)

# acho que pode tirar
    def rollD4(self):
        return random.randint(1,4)

    def rollD6(self):
        return random.randint(1,6)
    
    def rollD20(self):
        return random.randint(1,20)
# coloca a funçao dano aqui ou na fase de ataque?
  #  def dano(self,HP,AP,WP,type):
   

# personagens do player
c1 = Characters(32,5,2,5,2,'warrior')
c2 = Characters(20,25,0,2,5,'priest')
# inimigos
e1 = Characters(15,0,2,2,2,'orcWarrior1')
e2 = Characters(15,0,2,2,2,'orcWarrior2')
e3 = Characters(15,0,2,2,2,'orcWarrior3')
e4 = Characters(15,0,2,2,2,'orcWarrior4')

# gasto de MP
if c1.canSpell(1):
    c1.MP -= 5
    # COLOCA AQUI UM IF pra saber em qual inimigo vai dar dano. (colocar dps de codar o input pra escolher)
        #e1.HP -= c1.spellEffect_1() #como dar dano no e1,e2,e3, ou e4?
if c2.canSpell(1):
    c2.MP -= 5
if c2.canSpell(2):
    c2.MP -= 3 

#rolagem de dados
d4 = c1.rollDice(4)
d6 = c1.rollDice(6)
d20 = c1.rollDice(20)
# rolagem de dados para os spells
c1.spellEffect_1(d4)
c2.spellEffect_1(d4)
c2.spellEffect_2(d6)


while run:
        # INTRO #
    base()
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

    # se precisa de mais detalhes
    info = str(input("\n > Do you need more info about HP, MP, AP, WP and Init?(Y/N) > "))
    if info == str('Y') or str("y"):
        print("info to be made")
    elif info == str('N') or str('n'):
        continue
    print(" Great! So let's get started! \n")
    # Começo do Turno
    #print("") > ESCREVA AQUI INTRODUÇÃO A BATALHA
    def initwho():
        warriorinit = c1.INIT
        priestinit = c2.INIT
        enemyinit = e1.INIT
        TurnWOrder = d20 + warriorinit
        TurnPOrder = d20 + priestinit
        TurnEOrder = d20 + enemyinit
        print(TurnWOrder,TurnPOrder,TurnEOrder)
        '''''
        all_init = [c1.INIT or c2.INIT or e1.INIT]
        for i in range(len(all_init)):
           TurnOrder = d20 + i
        print(i + TurnOrder)
        #oq ta acontecendo aqui?????? como saber qual dos 3 o numero saiu ali?
    initwho()
    '''
    initwho()



    


# encerrar 
    break
print(reset)

