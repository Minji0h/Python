import time


COINS = {'1c': 0.01, '5c': 0.05, '10c': 0.10,'25c': 0.25, '50c': 0.50, '1r': 1}
DIVIDER = "================================================="

class MoneyMachine():
    def __init__(self):
        self.money = 0.0

    #Classe que recebe as moedas
    def inserir_moeda(self, price):
        while(self.money < price):
            print(DIVIDER)
            moeda = input("Por gentileza, insira uma moeda: \nMoedas aceitas: 1c 5c 10c 25c 50c 1r \n")
            if(COINS.get(moeda)):
                self.money += COINS.get(moeda)
                self.money = round(self.money, 2)
            else:
                print(DIVIDER)
                print("Moeda não aceita")
                cancelar = input("Deseja cancelar a operação? \n 1 - Sim \n 2 - Não \n")
                print(DIVIDER)
                if(cancelar == "1"):
                    break

    def consumir_saldo(self, quantia):
        self.money = round((self.money-quantia),2)

    #Classe para a consulta de saldo
    def consulta_saldo(self):
        return self.money
    
    #Classe que retorna o troco
    def devolve_troco(self):
        troco = False
        while(self.money != 0):
            time.sleep(0.5)
            troco = True
            if(self.money >= 1):
                print("              ┌───────────┐                 \n             ┌┘           └┐                \n            ┌┘     ┌┐      └┐               \n            │     ┌┘│       │               \n            │     └┐│┌─┐    │               \n            │      │││┌┘    │               \n            │     ┌┘└┤│     │               \n            └┐    └──┴┘    ┌┘               \n             └┐           ┌┘                \n              └───────────┘                 ")
                self.money = round(self.money - 1,2)
            elif(self.money >= 0.5):
                print("              ┌───────────┐                 \n             ┌┘           └┐                \n            ┌┘ ┌───┬───┐   └┐               \n            │  │┌──┤┌─┐│    │               \n            │  │└──┤│││├──┐ │               \n            │  └──┐│││││┌─┘ │               \n            │  ┌──┘│└─┘│└─┐ │               \n            └┐ └───┴───┴──┘┌┘               \n             └┐           ┌┘                \n              └───────────┘                 ")
                self.money = round(self.money - 0.50,2)
            elif(self.money >= 0.25):
                print("              ┌───────────┐                 \n             ┌┘           └┐                \n            ┌┘ ┌───┬───┐   └┐               \n            │  │┌─┐│┌──┘    │               \n            │  └┘┌┘│└──┬──┐ │               \n            │  ┌─┘┌┴──┐│┌─┘ │               \n            │  ││└─┬──┘│└─┐ │               \n            └┐ └───┴───┴──┘┌┘               \n             └┐           ┌┘                \n              └───────────┘                 ")
                self.money = round(self.money - 0.25,2)
            elif(self.money >= 0.1):
                print("              ┌───────────┐                 \n             ┌┘           └┐                \n            ┌┘  ┌┐┌───┐    └┐               \n            │  ┌┘││┌─┐│     │               \n            │  └┐│││││├──┐  │               \n            │   │││││││┌─┘  │               \n            │  ┌┘└┤└─┘│└─┐  │               \n            └┐ └──┴───┴──┘ ┌┘               \n             └┐           ┌┘                \n              └───────────┘                 ")
                self.money = round(self.money - 0.10,2)
            elif(self.money>=0.05):
                print("              ┌───────────┐                 \n             ┌┘           └┐                \n            ┌┘  ┌───┐      └┐               \n            │   │┌──┘       │               \n            │   │└──┬──┐    │               \n            │   └──┐│┌─┘    │               \n            │   ┌──┘│└─┐    │               \n            └┐  └───┴──┘   ┌┘               \n             └┐           ┌┘                \n              └───────────┘                 ")
                self.money = round(self.money - 0.05,2)
            elif(self.money>=0.01):
                print("              ┌───────────┐                 \n             ┌┘           └┐                \n            ┌┘    ┌┐       └┐               \n            │    ┌┘│        │               \n            │    └┐│┌──┐    │               \n            │     │││┌─┘    │               \n            │    ┌┘└┤└─┐    │               \n            └┐   └──┴──┘   ┌┘               \n             └┐           ┌┘                \n              └───────────┘                 ")
                self.money = round(self.money - 0.01,2)
            else:
                self.money = 0
        return troco
