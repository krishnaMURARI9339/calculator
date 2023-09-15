print("--Simple  calculator--\n")

firstNum = float(input("Enter a 1st number ="))
secondNum = float(input("Enter a 2nd number = "))

print("Press 1 for addition\n")
print("Press 2 for Subtration\n")
print("Press 3 for Multiply\n")
print("Press 4 for Divide\n")

userChoice = int(input("press 1 - 4 for calculation"))

if userChoice == 1:
    print("Sum of two number is ", firstNum +secondNum)
elif userChoice == 2:
    print("Subtration of two number is ",firstNum-secondNum)
elif userChoice == 3:
    print("Multifly of two number is ", firstNum* secondNum)
elif userChoice == 4:
    print("Divide of two number is", firstNum/secondNum)
else :
    print("Invalid  user input")


