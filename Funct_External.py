# Run function from external script

# from Function_Testing import spell_name

# user_name = input("Please enter your first name: ")

# name_length = spell_name(user_name)

# print(f"You have {name_length} characters in your name.")

# ~~~---~~~

#from func_Calc import *

select_loop = 0
valid = 0

while select_loop == 0:
    print("Please make a selection.\n\n1. Addition\n2. Subtraction\n3. Multiplication\n4. Division\n")
    selection = input("Selection: ")

    if selection == "1" or selection == "Addition" or selection == "addition":
        str_selection = "Addition"
        select_loop = 1
        from func_Calc import add_num
    elif selection == "2" or selection == "Subtraction" or selection == "subtraction":
        str_selection = "Subtraction"
        select_loop = 1
        from func_Calc import sub_num
    elif selection == "3" or selection == "Multiplication" or selection == "multiplication":
        str_selection = "Multiplcation"
        select_loop = 1
        from func_Calc import mul_num
    elif selection == "4" or selection == "Division" or selection == "division":
        str_selection = "Divison"
        select_loop = 1
        from func_Calc import div_num
    else:
        print("**Error**\nInvalid input. Please input either a number (1-4) or the word for the selection you wish to make\n")
        select_loop = 0

    print(f"\nYou have selected {str_selection}. Please enter in the two numbers you would like to calculate.\n")
    num1 = input("number 1: ")
    num2 = input("number 2: ")

    if str_selection == "Addition":
        ans = add_num(num1, num2)
    elif str_selection == "Subtraction":
        ans = sub_num(num1, num2)
    elif str_selection == "Multiplcation":
        ans = mul_num(num1, num2)
    elif str_selection == "Divison":
        ans = div_num(num1, num2)

    print(f"The answer is {ans}.")