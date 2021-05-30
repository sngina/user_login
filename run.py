from user import Credential, Login

def user_login(user_name,password): # user login
    
    return Login.login(user_name,password)
    
def save_user(user):
    user.save_user()
def delete_credential(user): # user delete credentials.
    user.delete_credential()
def display_credentials():
    return Credential.display_credential()
def find_user(user):
    return Login.login(user)
def create_credentials(fname,lname,phone,email,password): #user creating an account.
    new_user = Credential(fname,lname,phone,email,password)
    return new_user
def save_credentials(credentials) :  
    credentials.save_credentials() 
def main(): #add a while loop for password..
    while True:
        print("Hello Welcome to your account.What is your user name?")
        print("Login...")
        user_name = input()
        print(f"Hello  {user_name}.Please insert your password")
        password = input()
        print('\n')
        l_user = user_login(user_name,password)
        if  l_user:
            print(f"{l_user.first_name} {l_user.last_name} Successfully logged in!")
            break #breaks if the password is correct
        else:
            print("Invalid user name or password!")
        
    while True:
        print("Use the short codes:cc - create a new user name,dc- display credentials,fu- find user,su-save user")
        short_code = input().lower()
        if short_code == 'cc':
                print("New user")
                print("-"*10)
                print("First name....")
                f_name = input()
                print("Last name")
                l_name =input()
                print("Phone number....")
                p_number = input()
                print("Email address...")
                e_address = input()
                print("New password...")
                password = input()
                save_credentials(create_credentials(f_name,l_name,p_number,e_address,password)) # create a new user.
                print(f"{f_name} {password}account created successfully!")

        elif    short_code == 'dc':
            if  display_credentials():
                print("Hey here is a list of all the credentials")
                print("\n")
                for credentials  in display_credentials():
                    print(f"{credentials.first_name} {credentials.second_name}...{credentials.phone_number}....{credentials.password}")
                    print('\n')

            else:
                print('\n')
                print("You don't have an account saved")
                print('\n')
        elif    short_code == 'fu':
                print("Enter the user name you want to search for")
                search_user = input()
                if find_user(search_user):
                    search_user = find_user(search_user)
                    print(f"{search_user.first_name} {search_user.password}")
                else:
                    print("The user name does not exist")

            

# login()
if  __name__ == '__main__':
    main()