from moneymachine import MoneyMachine
import json
import time
from coffee import Coffee
from tqdm import tqdm

from moneymachine import MoneyMachine
# -*- coding: utf-8 -*-
MAX_COFFEE = 100
MAX_WATER = 1000
MAX_MILK = 1000

DIVIDER = "================================================="

DRINKS = open("drinks.json", "r")
DRINKS = DRINKS.read()
DRINKS = json.loads(DRINKS)


class CoffeeMachine():
    def __init__(self):

        # Inicia a maquina com os valores de agua, leite e café
        self.water = MAX_WATER
        self.milk = MAX_MILK
        self.coffee = MAX_COFFEE
        self.cardapio = []
        self.money_machine = MoneyMachine()

        # Inicia o cardapio de bebidas
        for drink in DRINKS:
            name = drink["name"]
            price = drink["price"]
            ingredients = {
                "water": drink["water"], "coffee": drink["coffee"], "milk": drink["milk"], "cocoa": drink["cocoa"], "chantilly": drink["chantilly"]}
            self.cardapio.append(Coffee(name, price, 150, ingredients))

    # Busca os ingredientes das bebidas
    def get_ingredients(self, drinkname):
        exists = False
        for drink in self.cardapio:
            if(drink.name == drinkname):
                drink.print_ingredients()
                exists = True
                break
        if(exists == False):
            print("Bebida não encontrada")

    # Comprar uma bebida
    def buy_a_drink(self, drinkname):
        exists = False
        for drink in self.cardapio:
            if(drink.name == drinkname):
                if(drink.valida_insumos(self.milk, self.water, self.coffee)):
                    price = drink.price
                    if(self.money_machine.consulta_saldo() < price):
                        self.money_machine.inserir_moeda(price)
                    if(self.money_machine.consulta_saldo() >= price):
                        self.money_machine.consumir_saldo(price)
                        self.water -= drink.get_ingredient("water")
                        self.milk -= drink.get_ingredient("milk")
                        self.coffee -= drink.get_ingredient("coffee")
                        drink.print_coffee()
                        time.sleep(1)
                exists = True
                break
        if(exists == False):
            print("Bebida não encontrada")

    def print_cardapio(self):
        print(DIVIDER)
        print("Bebida                        Preço")
        print(DIVIDER)
        for drink in self.cardapio:
            print(f'{drink.name: <30}R${drink.price}')
        print(DIVIDER)
        time.sleep(1)

    def reabastecer_maquina(self):
        if(self.milk != MAX_MILK):
            print("Reabastecendo o leite: ")
            for i in tqdm(range(100), desc=False, ascii=" ♥", ncols=50):
                time.sleep(0.02)
            self.milk = MAX_MILK
        else:
            print("Leite em 100%!")
        if(self.water != MAX_WATER):
            print("Reabastecendo a água: ")
            for i in tqdm(range(100), desc=False, ascii=" ♥", ncols=50):
                time.sleep(0.02)
            self.water = MAX_WATER
        else:
            print("Água em 100%!")
        if(self.coffee != MAX_COFFEE):
            print("Reabastecendo o café: ")
            for i in tqdm(range(100), desc=False, ascii=" ♥", ncols=50):
                time.sleep(0.02)
            self.coffee = MAX_COFFEE
        else:
            print("Café em 100%!")

    def receber_troco(self):
        print(DIVIDER)
        troco = self.money_machine.devolve_troco()
        if(not troco):
            print("Você não tem troco a receber")
        print(DIVIDER)

    def print_machine_status(self):
        print(DIVIDER)
        print("                STATUS DA MAQUINA               ")
        print(DIVIDER)
        print(
            f"Quantidade de café: {self.coffee} g \nQuantidade de leite: {self.milk} ml \nQuantidade de água: {self.water} ml \nSaldo: R${self.money_machine.consulta_saldo()}")
        print(DIVIDER)
