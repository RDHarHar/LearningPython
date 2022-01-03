# Run function from external script

from Function_Testing import spell_name

user_name = input("Please enter your first name: ")

name_length = spell_name(user_name)

print(f"You have {name_length} characters in your name.")