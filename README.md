# User Login

#### Created on 29th May 2021
#### By Stella

## Description 

A terminal based application that enable users to manage their individual passwords and also generate new passwords for them if they Want

What Can the Appication do:

* Create a password locker account with their details, a login username and password with authenication

* Can store credentials for already existing accounts

* Create new Account credentials in the Application


* Can view saved accounts 

* Delete option for a specific Credential using login name(which is unique for all services)




---

## Run Application
Need an Terminal (Mac or Linux) or Command Prompt(Windows)

To run this project, please follow the following instructions.
* Get access to the internet.
* Clone the repository.

      $ git clone `https://github.com/sngina/user_login.git`
      $ cd password_locker

* To run the application, in your terminal:

        $ python3.6 run.py
        $ ./run.py

## Testing the Application
* To run the tests for the application file:

        $ python3 run.py

---

| Behaviour | Input | Output |
| :---------------- | :---------------: | ------------------: |
| Welcomes user to the applicatin | **In terminal: $./run.py** | Welcome Message. Username & Password? |
| Register If new | **Would you like to create a new account** | Provide username, firstname, lastname, phone number, email, password |
| Display menu Navigation | **What would you like to do?** | Use these codes : new - create a new credential, display - display credentials, delete - delete a credential,   the Application  |
| Prompt for creating new Credential | **Enter: new** | Enter the required form Account type, login name, email, site Url, password |
| Prompt for Diplay stored Credentials | **Enter: display** | list Available Credentials |
| Prompt for Deleting a Credential | **Enter: delete** | Credential deleted successfully |



---
## Technologies Used
Project is created with:
* Python 3.6 +

---

## Bugs

None at the moment, but would love to hear your feedback!

---

## Contact Details
For any inquiries, please reach out to

sngina707@gmail.com



---

### License
This Project is under the [MIT](LICENSE) license