import random

print("Welcome to Camel!")
print("You have stolen a camel to make your way across the great Mobi desert.")
print("The natives want their camel back and are chasing you down! Survive your")
print("desert trek and outrun the natives.")
print()

done = False
miles_traveled = 0
thirst = 0
camel_tiredness = 0
natives_distance = -20
drinks_in_canteen = 3

while not done:
    print("A. Drink from your canteen.")
    print("B. Ahead moderate speed.")
    print("C. Ahead full speed.")
    print("D. Stop and rest.")
    print("E. Status check.")
    print("Q. Quit.")
    
    choice = input("Your choice? ")
    choice = choice.upper()

    if choice == 'Q':
        done = True
    elif choice == 'E':
        print("Miles Traveled: ", miles_traveled)
        print("Drinks in canteen: ", drinks_in_canteen)
        print("The natives are ", miles_traveled-natives_distance , " miles behind you.")
    elif choice == 'D':
        camel_tiredness = 0
        print("The camel is happy.")
        natives_distance += random.randint(7, 14)