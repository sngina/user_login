#!/usr/bin/env python3.6
from user import Credential, Login
import random
import string
import os
def user_login(user_name,password): # user login
    
    return Login.login(user_name,password)
    
def save_user(user):
    user.save_user()
def delete_credential(user): # user delete credentials.
    Credential.delete_credential(user)
def display_credentials():
    return Credential.display_credential()
def find_user(user):
    return Credential.find_user(user)
def create_credentials(fname,lname,phone,email,password): #user creating an account.
    new_user = Credential(fname,lname,phone,email,password)
    return new_user
def save_credentials(credentials) :  
    credentials.save_credentials()
def password_gen():
    print("Do you want a system generated password?(yes/no)")
    test_user=input()
    if test_user== 'yes':
        print("Password Generated!")
        password = gen_pass()
        return password
    elif test_user == 'no' :

        print("Add your custom password?")

        hash_pass =input()
        return hash_pass
    else:
        print('Didnt catch what you wrote Pardon :)')
        password_gen()
    

        
def gen_pass():
    '''
      a method that returns a random password with 20 charaters hard to guess
    '''
    passwd = ''
    symbols = ['*', '%', '£']

    for _ in range(5):
      passwd += random.choice(string.ascii_lowercase)
      passwd += random.choice(string.ascii_uppercase)
      passwd += random.choice(string.digits)
      passwd += random.choice(symbols)
    return passwd           
def main(): #add a while loop for password..
    
        print("Hello Welcome to your account.What is your user name?")
        print("Login...")
        user_name = input()
        print(f"Hello  {user_name}.Please insert your password")
        password = input()
        print('\n')
        l_user = user_login(user_name,password)
        if  l_user:
            print(f"{l_user.first_name} {l_user.last_name} Successfully logged in!")
             #breaks if the password is correct
        
     
            while True:
                print("Use the short codes:cc - create a new user name,dc- display credentials,fu- find user,ru-remove user")
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
                    hash_wrd = password_gen()
                    save_credentials(create_credentials(f_name,l_name,p_number,e_address,hash_wrd)) # create a new user.
                    print(f"{f_name}   account created successfully!")

                elif    short_code == 'dc': # function of displayin an account
                    if  display_credentials():
                        print("Hey here is a list of all the credentials")
                        print("\n")
                        for credentials  in display_credentials():
                            print(f"{credentials.first_name} {credentials.last_name}...{credentials.phone_number}....{credentials.password}")
                            print('\n')

                    else:
                        print('\n')
                        print("You don't have an account saved")
                        print('\n')
                elif    short_code == 'fu': #function of finding an account
                    print("Enter the user name you want to search for")
                    user_name = input()
                    print("\n")
                    # print("Enter user's password")
                    # user_password = input()

                    if find_user(user_name):
                        search_user = find_user(user_name)
                        print(f"{search_user.first_name} {search_user.last_name} {search_user.email}{search_user.password}")
                        print('-'*20)
                    else:
                        print("The user name does not exist")
                elif    short_code == 'ru': # function for removing use
                    print("Enter the user name ")
                    delete_username = input('Firstname: ')
                    
                    f_user = find_user(delete_username)
                    if f_user !=None:
                        print(f"Are you sure you want to delete {f_user.first_name} ? (y/n)")
                        user_prompt = input().lower()
                        if user_prompt == "y":
                            delete_credential(f_user)
                        elif user_prompt =="n":
                            continue
                        else:
                            print("din't catch what you said..")
                            continue
                    else:
                            print("User doesn't exist")
        else:
            print("Invalid user name or password!")


                
                
# login()
if  __name__ == '__main__':
    main()