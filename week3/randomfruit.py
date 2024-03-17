# This program prints out a random fruit
import random
fruits = ['Pineapple', 'Passion Fruit', 'Kiwi', 'Strawberry']
# we want a random number between 0 and lenght-1
index = random.randint(0,len(fruits)-1)
fruit = fruits[index]
print("Here goes a Random Fruit: {}".format(fruit))