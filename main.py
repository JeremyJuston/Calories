import os

def recap():

    food_type = ""
    food = []

    while (food_type != "!"):
        food_type = input("What did you eat today ? ")
        food_qty = input("How many grams did you eat ? ")
        food.append([food_type, food_qty])

    food.pop()
    print(food)
    return food


def macro_calcul(food):

    prot = 0
    lip = 0
    glu = 0

    for i, food_data in enumerate(food):
        food_type = food_data[0]
        food_qty = int(food_data[1])
        
        print(food_type)
        print(food_qty)
        print("hey")

        food_prot = 1 * food_qty / 100
        food_lip = 2 * food_qty / 100
        food_glu = 3 * food_qty / 100

        food[i].append(food_prot)
        food[i].append(food_lip)
        food[i].append(food_glu)

        food[i].append(food_prot * 4 + food_lip * 9 + food_glu * 4)




def main ():
    print("hrllo")
    food = recap()
    macro_calcul(food)
    print(food)

main()

