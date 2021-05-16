""" 
File: prove02.py
Author: NO

Purpuse: program that asks the user for a series of words and then displays the story with the user's words
"""

print('Please enter the following: \n')
adjective = input('adjective: ')
animal = input('animal: ')
verb1 =  input('verb: ')
exclamation =  input('exclamation: ')
verb2 = input('verb: ')
verb3 = input('verb: ')
place = input('place :')
meal = input('meal: ')
beverage = input('beverage: ')

print ("\nYour story is:")

print(f'The other day, I was really in trouble. It all started when I saw a very {adjective} {animal} {verb1} down the hallway. "{exclamation.capitalize()}" I yelled. But all I could think to do was to {verb2} over and over. Miraculously, that caused it to stop, but not before it tried to {verb3} right in front of my family.')

print(f'\nWhat an interesting experience I thought, the truth is that I would like to be in {place.capitalize()}, eating {meal} and drinking {beverage}, how wonderful it would be. ')