from user import Login

def login(): # user login
    print("Please add your username and password!")
    user_name = input("Enter username: ")
    password = input("Enter your password: ")
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
    print(f"Hello{user_name}.Please insert your password")
    print("\n")
    password = input()


login()