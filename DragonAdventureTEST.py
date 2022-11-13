'''''
import random

reset = '\033[0m'
bold = '\033[01m'
underline = '\033[04m'
# efeitos de texto (letra)
darkgrey = '\033[90m'
# efeitos de texto(cor da letra)
lightgrey_bg = '\033[47m'
#efeitos de cor(fundo)
run = True


def initwho():
    TurnOrder = d20 + Init
    if 

def damage(enemy,valdamage):
    enemy["HP"] -= valdamage
    if enemy["HP"] < 0:
        enemy["HP"] = 0
    return enemy
def printstats(enemy):
    print("hp:",enemy["HP"],"AP",enemy["AP"])


priest = damage(priest,2)
warrior = damage(warrior,3)
printstats(priest)
printstats(warrior)

warrior["HP"] += 5

def base():
	return(print(reset + lightgrey_bg + darkgrey))
# função para manter as cores


# INTRO #
base()
print(bold + " Welcome to the Dragon Adventure World, warrior!"), base()
print(" You are in the middle of a battle, so you must be careful. But," + bold + " DON'T PANIC!")
base()
print(' You are not alone.\n Know your team:\n ')
print(bold + "  WARRIOR")
base()
print(" HP: 32 \n MP: 5 \n AP: 2 \n WP: 5 \n Init: 2 \n ")
print(bold + "  PRIEST")
base()
print(" HP: 20 \n MP: 25 \n AP: 0 \n WP: 2 \n Init: 6")

# + INFO ABOUT CHARACTERS
'''
'''''
info = str(input("\n Do you need more info about HP, MP, AP, WP and Init?(Y/N) > "))
if info == str('Y') or str("y"):
    print("info to be made")
elif info == str('N') or str('n'):
    print("So let's get started!")
'''


