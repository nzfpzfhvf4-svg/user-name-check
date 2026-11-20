#Usernames must adhere to following requirements:
#Between 5 and 15 characters
#Only contain letters, and no numbers

def username_choice(username):
    if  username.isalpha() == False:
        print("username cannot contain numbers")
    elif len(username) < 5:
        print("Usernames must be more than 5 characters")
    elif len(username) > 15:
        print("Usernames must be less than 15 characters")
    else:
        print("User name choice is great")

#asks user for their user name 
user_response = input("Enter your username choice: ")

#'moves' the user response to the function to check if compatable 
username_choice(user_response)


