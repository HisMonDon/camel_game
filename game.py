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
drinks_in_canteen = 5

while not done:
    print("A. Drink from your canteen.")
    print("B. Ahead moderate speed.")
    print("C. Ahead full speed.")
    print("D. Stop and rest.")
    print("E. Status check.")
    print("Q. Quit.")

    choice = input("Your choice? ")
    print()
    choice = choice.upper()

    if choice == 'Q':
        done = True
    elif choice == 'E':
        print("YOUR STATUS\n______________________")

        print("Miles Traveled:", miles_traveled)
        print("Drinks in canteen:", drinks_in_canteen)
        print("The natives are", miles_traveled - natives_distance, "miles behind you.")
    elif choice == 'D':
        camel_tiredness = 0
        print("The camel is happy.")
        natives_distance += random.randint(7, 14)
    elif choice == 'C':
        miles_traveled += random.randint(10, 20)
        print("You've traveled", miles_traveled, "miles.")
        thirst += 1
        camel_tiredness += random.randint(1, 3)
        natives_distance += random.randint(7, 14)
    elif choice == 'B':
        miles_traveled += random.randint(5, 12)
        print("You've traveled", miles_traveled, "miles.")
        thirst += 1
        camel_tiredness += 1
        natives_distance += random.randint(7, 14)
    elif choice == 'A':
        if drinks_in_canteen > 0:
            drinks_in_canteen -= 1
            thirst = 0
        else:
            print("You have no water.")

    if random.randint(1, 20) == 1:
        print("You found an oasis!")
        drinks_in_canteen = 3
        thirst = 0
        camel_tiredness = 0

    if miles_traveled >= 200:
        print("You made it across the desert! You won!")
        done = True

    if not done:
        if thirst > 6:
            print("You died of thirst!")
            done = True
        elif thirst > 4:
            print("You are thirsty.")

    if not done:
        if camel_tiredness > 8:
            print("Your camel is dead.")
            done = True
        elif camel_tiredness > 5:
            print("Your camel is getting tired.")

    if not done:
        if natives_distance >= miles_traveled:
            print("The natives have caught up!")
            done = True
        elif miles_traveled - natives_distance < 15:
            print("The natives are getting close!")
    randomnumber = random.randint(1, 20)
    if randomnumber == 5:
        camel_tiredness = 0
        thirst = 0
        drinks_in_canteen = 5
    if miles_traveled >= 200:
        done = True
    print("")