class   Login:
    def __init__(self,first_name,last_name,phone_number,email,password):
        self.first_name =first_name
        self.last_name = last_name
        self.phone_number = phone_number
        self.email = email
        self.password = password
    login_list = []
    def save_user(self) :
        Login.login_list.append(self)
    def delete_credential(self) :
        Login.login_list.remove(self)
    @classmethod
    def display_credential(cls):
        return cls.login_list
    
    
# Login.save_user("name")

# print(Login.login_list)
# Login.delete_contact("name")