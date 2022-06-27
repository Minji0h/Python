
import time
from tkinter import ROUND
from car import Car
import random


class Car_manager:

    #Inicia o Car Manager
    def __init__(self):
        self.cars = []
        self.max_cars = 10
        self.level = 1
        self.init_cars()
        self.cars_speed = 0.1

    #Função para iniciar os carros
    def init_cars(self):
        self.max_cars = 10 * self.level + 1
        for i in range(self.level + 3):
            self.cars.append(Car())
    
    #Função para atualizar para o proximo nivel
    def next_level(self):
        self.level = self.level + 1
        self.cars_speed = self.cars_speed * 0.9
        self.clear_cars()
        self.init_cars()
    
    #Função para mover os carros
    def manager_cars(self):
        self.new_car()
        for car in self.cars:
            car.still_car_in_screen()
            car.move_car()
        time.sleep(self.cars_speed)
    
    #Função que randomiza quando um novo carro devera aparecer em tela
    def new_car(self):
        if(random.randint(0, 5) ==  1 and len(self.cars) <= self.max_cars):
            self.cars.append(Car())
    
    #Função que valida se houve uma batida
    def validate_crash(self, player):
        for car in self.cars:
            if car.distance(player) < 30:
                return True
        return False

    #Função que limpa os carros da tela
    def clear_cars(self):
        for car in self.cars:
            car.hideturtle()
        self.cars = []
