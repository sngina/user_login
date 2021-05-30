class   Login:
    def __init__(self,first_name,last_name,phone_number,email,password):
        self.first_name =first_name
        self.last_name = last_name
        self.phone_number = phone_number
        self.email = email
        self.password = password
    login_list = [] #empty login list

    
    
    # login method for the user
    @classmethod
    def login(cls,user_name,password) :
        for user in cls.login_list:
            if user.first_name == user_name and user.password == password:
                return user
        

            
        # print(user_name)
        # print(password)
    # save method for the user
    def save_user(self) :
        Login.login_list.append(self)
        print("Saved!")
    
    
    # Create an account.
    
class Credential:
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
    def delete_credential(self) :
        Login.login_list.remove(self)
    @classmethod
    def display_credential(cls):
        return cls.login_list

new_user = Login("Peter","Ken","073456723","Ken@gmail.com","maya@2013!")
Login.login_list.append(new_user)
# Login.login() 
# Login.save_user("name")


# Login.delete_contact("name")