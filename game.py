# 1
print("Welcome to Camel!")
print("You have stolen a camel to make your way across the great Mobi desert.")
print("The natives want their camel back and are chasing you down! Survive your")
print("desert trek and outrun the natives.")
print()

# 2
done = False
# 8
miles_traveled = 0
thirst = 0
camel_tiredness = 0
# 9
natives_distance = -20
# 10
drinks_in_canteen = 3

# 3
while not done:
    # 4
    print("A. Drink from your canteen.")
    print("B. Ahead moderate speed.")
    print("C. Ahead full speed.")
    print("D. Stop and rest.")
    print("E. Status check.")
    print("Q. Quit.")
    
    # 5
    choice = input("Your choice? ")
    # 6
    choice = choice.upper()

    if choice == 'Q':
        done = True
    # 11
    elif choice == 'E':
        print("Miles Traveled: ", miles_traveled)
        print("Drinks in canteen: ", drinks_in_canteen)
        print("The natives are ", miles_traveled-natives_distance , " miles behind you.")
    elif choice == ''



