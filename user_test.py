from typing import ClassVar
import unittest
from   user import  Login

class  TestLogin(unittest.TestCase):
    def setup(self):
        self.login = Login("Stella","Ngina","0726091999","sngina707@gmail.com,munie")
    def test_init(self):
        self.assertEqual(self.login.first_name,"Stella") 
        self.assertEqual(self.login.last_name,"Ngina")
        self.assertEqual(self.login.phone_number,"0726091999")
        self.assertEqual(self.login.email,"sngina707@gmail.com")
        self.assertEqual(self.login.password,"munie")