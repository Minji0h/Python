from ctypes import sizeof
from mimetypes import init
import time
from tqdm import tqdm
# -*- coding: utf-8 -*-
DIVIDER = "================================================="


class Coffee():
    def __init__(self, name, price, size, ingredients):
        self.name = name
        self.price = price
        self.size = size
        self.ingredients = ingredients
    
    def valida_insumos(self, milk, water, coffee):
        if(self.ingredients['milk'] <= milk and self.ingredients['water'] <= water and self.ingredients['coffee'] <= coffee): 
            return True
        else:
            print(DIVIDER)
            print("Ingredientes insuficientes! Por gentileza, reabasteça a maquina")
            print(DIVIDER)
            return False

    def print_ingredients(self):
        milk = self.ingredients['milk']
        water = self.ingredients['water']
        coffee = self.ingredients['coffee']
        cocoa = self.ingredients['cocoa']
        chantilly = self.ingredients['chantilly']

        string = ''
        if(milk != 0):
            string += f'Leite: {milk} ml    '
        if(water != 0):
            string += f'Água: {water} ml    '
        if(coffee != 0):
            string += f'Café: {coffee} g    '
        if(cocoa != 0):
            string += f'Chocolate: {cocoa} g    '
        if(chantilly != 0):
            string += f'Chantilly     '


        print(DIVIDER)
        print(string)
        print(DIVIDER)

    def get_ingredient(self, ingredient_name):
        return self.ingredients.get(ingredient_name, "Ingrediente não encontrado!")

    def print_coffee(self):
        print(DIVIDER)
        print("           **Preparando a bebida**               ")
        print(DIVIDER)
        for i in tqdm(range(100), desc=False, ascii=" ♥", ncols=50):
            time.sleep(0.02)
        print(DIVIDER)
        print("               **Bebida pronta**                 ")
        print(DIVIDER)
        print("                 }___{ ___{                      ")
        print("              .-{    }     }-.                   ")
        print("             (   }        {   )                  ")
        print("             |`-.________..-'|                   ")
        print("             |                ;--.               ")
        print("             |               (__  \              ")
        print("             |                | )  )             ")
        print("             |                |/  /              ")
        print("             |                /  /               ")
        print("             |               (  /                ")
        print("             \                y'                 ")
        print("              `-..________..-'                   ")
        print(DIVIDER)
