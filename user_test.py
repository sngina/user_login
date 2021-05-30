
from run import save_user
import unittest
from   user import  Login

class  TestLogin(unittest.TestCase):
    def setUp(self): #first setup
        self.login = Login("Stella","Ngina","0726091999","sngina707@gmail.com","munie")
    def test_init(self):
        self.assertEqual(self.login.first_name,"Stella") 
        self.assertEqual(self.login.last_name,"Ngina")
        self.assertEqual(self.login.phone_number,"0726091999")
        self.assertEqual(self.login.email,"sngina707@gmail.com")
        self.assertEqual(self.login.password,"munie")
     
    
    def test_save_multiple_user(self): #test multiple save
        self.create_credentials.save_user()
        test_user = Login("Test","user","0721345678","test@user") # new contact
        test_user.save_user()
        self.assertEqual(len(Login.login_list),2)
    def tearDown(self):
        Login.login_list = []
    


if __name__ == '__main__':
    unittest.main()