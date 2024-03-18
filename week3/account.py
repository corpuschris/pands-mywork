#that reads in a 10 character account number and outputs 
#the account number with only the last 4 digits showing 
#(and the first 6 digits replaced with Xs).
#Author: Christiano Ferreira

AccNumber = input("Please enter an 10 digit account number:" )

print (f'XXXXXX{AccNumber[6:10]}')