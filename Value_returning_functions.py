import math


def price():
    while True:
        price = int(input("How old is this person?: "))
        if price > 62:
            total1 = 20
            break
        elif price > 13 <= 62:
            total2 = 25
            break
        elif price > 3 <= 12:
            total3 = 15
            break
        elif price < 3:
            total4 = 0
            break
        print("Let's try this again. ")
    return price


numPeople = int(input("How many people are in your group?: "))
for age in range(1, numPeople + 1):
    price = numPeople
    total = 0
    while True:
        price = int(input("How old is this person?: "))
        if price > 62:
            total1 = 20
            print("You owe: $", total1)
            break
        elif price > 13 <= 62:
            total2 = 25
            print("You owe: $", total2)
            break
        elif price > 3 <= 12:
            total3 = 15
            print("You owe: $", total3)
            break
        elif price < 3:
            total4 = 0
            print("You are free!")
            break