#this program  keeps reading numbers until the user enters a 0

#Author: Christiano Ferreira


numbers = []

number = int(input("Enter number (0 to quit): "))

while number != 0:
    numbers.append(number)

    number = int(input("Enter another (0 to quit): "))

for value in numbers:
    print (value)

average = float (sum(numbers)) / len(numbers)

print (f"The average is {average}")