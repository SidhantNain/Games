print("Hello there!! are you ready to challenge computer in rock, paper, scissor game?????\nSo, Lets start....")
print("First,Lets start with your choice. Please select your choice from given list.")
print("And remember best five will be counted!!!!")
print("1.Rock")
print("2.Paper")
print("3.Scissors")

from random import randint
for i in range(5):
    choice = int(input("Enter your choice = "))
    a = randint(1, 3)
    if choice == 1:
        if a == 1:
            print("Comp choose Rock\nmatch tied")
        elif a == 2:
            print("Comp choose Paper\nyou lost")
        else:
            print("Comp choose Scissor\nyou win")
    elif choice == 2:
        if a == 1:
            print("Comp choose Rock\nyou win")
        elif a == 2:
            print("Comp choose Paper\nmatch tied")
        else:
            print("Comp choose Scissor\nyou lost")
    elif choice == 3:
        if a == 1:
            print("Comp choose Rock\nyou lost")
        elif a == 2:
            print("Comp choose Paper\nyou win")
        else:
            print("Comp choose Scissor\nmatch tied")
    else:
        print("Enter Valid option")


