#Function Testing

def spell_name(user_name): 
    size = len(user_name)
    for i in range(size):
        print(user_name[i])
    return(size)

user_name = input("Please enter your first name: ")

name_length = spell_name(user_name)

print(f"You have {name_length} characters in your name.")