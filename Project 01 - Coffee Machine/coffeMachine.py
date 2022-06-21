from http.client import MOVED_PERMANENTLY
import json
import time
from turtle import pensize
from coffee import Coffee
from tqdm import tqdm 

MAX_COFFEE = 100
MAX_WATER = 1000
MAX_MILK = 1000

DIVIDER = "================================================="

DRINKS = open("drinks.json","r")
DRINKS = DRINKS.read()
DRINKS = json.loads(DRINKS)

COINS = {'1c': 0.01, '5c': 0.05, '10c': 0.10, '25c': 0.25, '50c': 0.50, '1r': 1}

class CoffeeMachine():
    def __init__(self):
        self.water = MAX_WATER
        self.milk = MAX_MILK
        self.coffee = MAX_COFFEE
        self.money = 0.0
        self.cardapio = []
        self.init_cardapio()

    def init_cardapio(self):
        for drink in DRINKS:
            name = drink["name"]
            price = drink["price"]
            ingredients =  {"water": drink["water"], "coffee": drink["coffee"], "milk": drink["milk"]}
            self.cardapio.append(Coffee(name, price, 150,ingredients))

    def get_ingredients(self, drinkname):
        exists = False
        for drink in self.cardapio:
            if(drink.name == drinkname):
                print(drink.print_ingredients())
                exists = True
                break
        if(exists == False): print("Bebida não encontrada")

    def buy_a_drink(self, drinkname):
        exists = False
        for drink in self.cardapio:
            if(drink.name == drinkname):
                water = drink.get_ingredient("water")
                milk = drink.get_ingredient("milk")
                coffee = drink.get_ingredient("coffee")
                price = round(drink.price, 2)
                if(self.water>=water and self.milk >= milk and self.coffee >= coffee):
                    if(self.money < price):
                        self.insert_coin(price)
                    if(self.money >= price):
                        self.money -= price
                        self.water -= water
                        self.milk -= milk
                        self.coffee -= coffee
                        drink.print_coffee()
                        time.sleep(1)
                else:
                    print(DIVIDER)
                    print("Ingredientes insuficientes! Por gentileza, aguarde a maquina recarregar, ou tente outra bebida.")
                    print(DIVIDER)
                exists = True
                break
        if(exists == False): print("Bebida não encontrada")
    
    def insert_coin(self, price):
        while(self.money < price):
            moeda = input("Por gentileza, insira uma moeda: \n Moedas aceitas: 1c 5c 10c 25c 50c 1r \n")
            if(COINS.get(moeda)):
                self.money += COINS.get(moeda)
                self.money = round(self.money, 2)
            else:
                print("Moeda não aceita")
                cancelar = input("Deseja cancelar a operação? \n 1 - Sim \n 2 - Não")
                if(cancelar == "1"): break


    def print_cardapio(self):
        print(DIVIDER)
        print("Bebida                        Preço")
        print(DIVIDER)
        for drink in self.cardapio:
            print(f'{drink.name: <30}R${drink.price}')
        print(DIVIDER)
    
    def reabastecer_maquina(self):
        if(self.milk == MAX_MILK and self.water == MAX_WATER and self.coffee == MAX_COFFEE):
            print("Todos os insumos já estão em 100%")
        if(self.milk != MAX_MILK):
            print("Reabastecendo o leite: ")
            for i in tqdm (range (100),desc=False, ascii =" ♥", ncols=50): time.sleep(0.02) 
        if(self.water != MAX_WATER):
            print("Reabastecendo a água: ")
            for i in tqdm (range (100),desc=False, ascii =" ♥", ncols=50): time.sleep(0.02) 
        if(self.coffee != MAX_COFFEE):
            print("Reabastecendo o café: ")
            for i in tqdm (range (100),desc=False, ascii =" ♥", ncols=50): time.sleep(0.02) 

    def print_machine_status(self):
        print(DIVIDER)
        print("                STATUS DA MAQUINA               ")
        print(DIVIDER)
        print(f"Quantidade de café: {self.coffee} g \nQuantidade de leite: {self.milk} ml \nQuantidade de água: {self.water} ml \nSaldo: R${self.money}")
        print(DIVIDER)