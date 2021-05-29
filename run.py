from user import Login

def login():
    print("Please add your username and password!")
    user_name = input("Enter username: ")
    password = input("Enter your password: ")
    Login.login(user_name,password)
def save_user(user):
    user.save_user()



login()