#this program asks the user to input any positive integer and outputs the successive values of the following calculation.

#Author: Christiano Ferreira


num = int(input("Enter a positive integer: "))
while num != 1:
    print (num, end=" ")
    num = num // 2 if num % 2 == 0 else num * 3 + 1
print (1)