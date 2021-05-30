from user import Login

def login(cls,user_name,password): # user login
    print("Please add your username and password!")
    user_name = input("Enter username: ")
    password = input("Enter your password: ")
    if cls.login_list[0] == user_name  and cls.login_list[4] == password:
            print("Okay!")
              
    else:
            print("Invalid user name and password!")
            
    Login.login(user_name,password)
def save_user(user):
    user.save_user()
def delete_credential(user): # user delete credentials.
    user.delete_credential()
def display_credantials(user):
    return Login.display_credential()
def find_user(user):
    return Login.login(user)
def create_credentials(fname,lname,phone,email,password): #user creating an account.
    new_user = Login(fname,lname,phone,email,password)
    return new_user
    
def main():
    print("Hello Welcome to your account.What is your user name?")
    user_name = input()
    print(f"Hello  {user_name}.Please insert your password")
    password = input()
    print('\n')
    while True:
        print("Use the short codes:cc - create a new user name,dc- display credentials,su-save user,fu- find user")
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
            print("Email addrss...")
            e_address = input()
            print("New password...")
            password = input()
            save_user(create_credentials(f_name,p_number,e_address,password)) # create a new user.
        elif    short_code == 'dc':
            if  display_credantials():
                print("Hey here is a list of all the credentials")
                print("\n")
                for login in display_credantials():
                    print(f"{login.first_name} {login.second_name}...{login.phone_number}....{login.password}")
                    print('\n')
            else:
                print('\n')
                print("You don't have an account saved")
                print('\n')

# login()
if  __name__ == '__main__':
    main()