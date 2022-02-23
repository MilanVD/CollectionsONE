from random import choice
import random

#Deel 1: Lists

colors = ["groen", "oranje", "blauw", "bruin"]

print("Hoeveel kleuren m&m's wil je aan de zak toevoegen?")
aantal = int(input("> "))


def listZak(aantal: int):
    colors_bag = []
    for i in range(aantal):
        color = choice(colors)
        colors_bag.append(color)
    else:
        return colors_bag

