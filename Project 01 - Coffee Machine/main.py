from coffemachine import CoffeeMachine

COFFEEMACHINE = CoffeeMachine()
DIVIDER = "================================================="

MENU = " 1 - Gostaria de ver o cardapio \n 2 - Gostaria de saber os ingredientes de uma bebida \n 3 - Gostaria de fazer um pedido \n 4 - Gostaria de receber meu troco \n 5 - Gostaria de reabastecer a maquina \n 6 - Gostaria de saber o status da maquina \n 0 - Sair"

def label():
    print("=======================================================================================================")
    print(" ____    __    ____  _______  __        ______   ______   .___  ___.  _______     )  (    )  (  (      ")
    print(" \   \  /  \  /   / |   ____||  |      /      | /  __  \  |   \/   | |   ____|    (  )   (   )  )      ")
    print("  \   \/    \/   /  |  |__   |  |     |  ,----'|  |  |  | |  \  /  | |  |__        ) (   )  (  (       ")
    print("   \            /   |   __|  |  |     |  |     |  |  |  | |  |\/|  | |   __|       ( )  (    ) )       ")
    print("    \    /\    /    |  |____ |  `----.|  `----.|  `--'  | |  |  |  | |  |____      _____________       ")
    print("     \__/  \__/     |_______||_______| \______| \______/  |__|  |__| |_______|    <_____________> ___  ")
    print("                            .___________.  ______                                 |             |/ _ \ ")
    print("                            |           | /  __  \                                |               | | |")
    print("                            `---|  |----`|  |  |  |                               |               |_| |")
    print("                                |  |     |  |  |  |                            ___|             |\___/ ")
    print("                                |  |     |  `--'  |                           /    \___________/    \  ")
    print("                                |__|      \______/                            \_____________________/  ")
    print("  .___________. __  .___  ___.  _______      ______   ______    _______  _______  _______  _______     ")
    print("  |           ||  | |   \/   | |   ____|    /      | /  __  \  |   ____||   ____||   ____||   ____|    ")
    print("  `---|  |----`|  | |  \  /  | |  |__      |  ,----'|  |  |  | |  |__   |  |__   |  |__   |  |__       ")
    print("      |  |     |  | |  |\/|  | |   __|     |  |     |  |  |  | |   __|  |   __|  |   __|  |   __|      ")
    print("      |  |     |  | |  |  |  | |  |____    |  `----.|  `--'  | |  |     |  |     |  |____ |  |____     ")
    print("      |__|     |__| |__|  |__| |_______|    \______| \______/  |__|     |__|     |_______||_______|    ")
    print("=======================================================================================================")

def init():
    label()


    a = input(f"O que deseja hoje? \n{DIVIDER}\n{MENU}\n{DIVIDER}\n")

    while a != "0":
        if(a == "1"):
            COFFEEMACHINE.print_cardapio()
        elif(a == "2"):
            drinkname = input("Qual o nome da bebida? \n")
            COFFEEMACHINE.get_ingredients(drinkname)
        elif(a == "3"):
            drinkname = input("Qual o nome da bebida? \n")
            COFFEEMACHINE.buy_a_drink(drinkname)
        elif(a == "4"):
            COFFEEMACHINE.receber_troco()
        elif(a == "5"):
            COFFEEMACHINE.reabastecer_maquina()
        elif(a == "6"):
            COFFEEMACHINE.print_machine_status()
        else:
            print(f"Desculpe, não entendi. Poderia olhar o menu novamente e escolher uma opção?\n{DIVIDER}")
        a = input(f"Posso ajudar em algo mais? \n{DIVIDER}\n{MENU}\n{DIVIDER}\n")
    print("Okay!! Espero que tenha gostado de nosso serviços :)")
    COFFEEMACHINE.receber_troco()


init()
