menu = """Please select one of the following options:
1) Add new entry for today.
2) View entries.
3) Exit.

Your selection: """

welcome = "Welcome to the programming diary!"

# user_input = input(menu)
# while user_input != "3":
#     user_input = input(menu)


print(welcome)


# The walrus operator, :=, can be read as "being equal.". 
# So the while loop means "while user_input, being equal to the user's input, is not equal to 3".
while (user_input := input(menu)) != "3":
    if user_input == "1":
        print("Adding...")
    elif user_input == "2":
        print("Viewing...")
    else:
        print("Invalid option, please try again!")