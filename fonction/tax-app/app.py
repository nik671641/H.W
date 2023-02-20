from tax import *
import os


print("\nEnter the dada that meets the requirements \n vvvvvvvvvvvvvvvvvvvvvvvvv")

amount_money = int(input('amount_money : '))
amount_percentage = int(input('amount_percentage : '))
amount_assignment = input('amount_assignment : ')
os.system('cls')
calculateTax(amount_money, amount_percentage, amount_assignment)
