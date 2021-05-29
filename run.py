from user import Login

def login():
    print("Please add your username and password!")
    user_name = input("Enter username: ")
    password = input("Enter your password: ")
    Login.login(user_name,password)



login()