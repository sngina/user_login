class   Login:
    def __init__(self,first_name,last_name,phone_number,email,password):
        self.first_name =first_name
        self.last_name = last_name
        self.phone_number = phone_number
        self.email = email
        self.password = password
    login_list = ["Stella","Ngina","0726091916","sngina707@gmail.com","Maingi"]
    
    # login method for the user
    @classmethod
    def login(cls,user_name,password) :
        if cls.login_list[0] == user_name  and cls.login_list[4] == password:
            print("Okay!")
              
        else:
            print("Invalid user name and password!")
        # print(user_name)
        # print(password)
    # save method for the user
    def save_user(self) :
        Login.login_list.append(self)
    def delete_credential(self) :
        Login.login_list.remove(self)
    @classmethod
    def display_credential(cls):
        return cls.login_list
    # Create an account.
    def create_credentials(self):
        print("Add your user name")
        print("\n") 
        user_name =  input("user name:  ")
        print("Add your number")
        print("\n")
        number = input("number: ")
        print("Add your email address")
        print("\n")
        email = ("email: ")
        print("Insert your new password")
        password = input("password: ")
# Login.login() 
# Login.save_user("name")


# Login.delete_contact("name")