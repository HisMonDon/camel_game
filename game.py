print("Welcome to Camel! \nYou have stolen a camel to make your way across the great Mobi desert.\nThe natives want their camel back and are chasing you down! Survive your\ndesert trek and out run the natives.")
done=False
miles_traveled = 0
thirst=0
camel_tiredness = 0
natives_distance = -20
drinks_in_canteen = 3
while not done:
    print("Choose your move:\nA. Drink from your canteen.\nB. Ahead moderate speed.\nC. Ahead full speed.\nD. Stop for the night.\nE. Status check.\nQ. Quit.")
    choice = input()
    choice = choice.upper()
    if choice == 'Q':
        done = True
    elif choice == 'E':
        print("Miles Traveled: ", miles_traveled)
        print("Drinks in canteen: ", drinks_in_canteen)
        print("The natives are ", miles_traveled-natives_distance , " miles behind you.")
    elif choice == ''



