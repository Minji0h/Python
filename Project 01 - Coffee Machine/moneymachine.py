COINS = {'1c': 0.01, '5c': 0.05, '10c': 0.10,'25c': 0.25, '50c': 0.50, '1r': 1}


class MoneyMachine():
    def __init__(self):
        self.money = 0.0

    #Classe que recebe as moedas
    def inserir_moeda(self, price):
        while(self.money < price):
            moeda = input("Por gentileza, insira uma moeda: \n Moedas aceitas: 1c 5c 10c 25c 50c 1r \n")
            if(COINS.get(moeda)):
                self.money += COINS.get(moeda)
                self.money = round(self.money, 2)
            else:
                print("Moeda não aceita")
                cancelar = input("Deseja cancelar a operação? \n 1 - Sim \n 2 - Não")
                if(cancelar == "1"):
                    break

    #Classe para a consulta de saldo
    def consulta_saldo(self):
        return self.money
    
    #Classe que retorna o troco
    def devolve_troco(self):
        troco = []
        while(self.money != 0):
            if(self.money >= 1):
                troco.append("1r")
                self.money -= 1
            elif(self.money >= 0.5):
                troco.append("50c")
                self.money -= 0.5
            elif(self.money >= 0.25):
                troco.append("25c")
                self.money -= 0.25
            elif(self.money >= 0.1):
                troco.append("10c")
                self.money -= 0.1
            elif(self.money>=0.05):
                troco.append("5c")
                self.money -= 0.05
            elif(self.money>=0.01):
                troco.append("1c")
                self.money -= 0.01
            else:
                self.money = 0
        return troco
