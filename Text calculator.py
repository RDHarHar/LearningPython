select_loop = 0
valid = 0

while select_loop == 0:
    print("Please make a selection.\n\n1. Addition\n2. Subtraction\n3. Multiplication\n4. Division\n")
    selection = input("Selection: ")

    if selection == "1" or selection == "Addition" or selection == "addition":
        str_selection = "addition"
        select_loop = 1
    elif selection == "2" or selection == "Subtraction" or selection == "subtraction":
        str_selection = "subtraction"
        select_loop = 1
    elif selection == "3" or selection == "Multiplication" or selection == "multiplication":
        str_selection = "multiplcation"
        select_loop = 1
    elif selection == "4" or selection == "Division" or selection == "division":
        str_selection = "divison"
        select_loop = 1
    else:
        print("**Error**\nInvalid input. Please input either a number (1-4) or the word for the selection you wish to make\n")
        select_loop = 0

    print(f"\nYou have selected {str_selection}. Please enter in the two numbers you would like to calculate.\n")
    num1 = input("number 1: ")
    num2 = input("number 2: ")

    if str_selection == "addition":
        ans = int(num1) + int(num2)
    elif str_selection == "subtraction":
        ans = int(num1) - int(num2)
    elif str_selection == "multiplcation":
        ans = int(num1) * int(num2)
    elif str_selection == "divison":
        ans = int(num1) / int(num2)

    print(f"The answer is {ans}.")