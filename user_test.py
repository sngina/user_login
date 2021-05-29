from typing import ClassVar
import unittest
from   user import  Login

class  TestLogin(unittest.TestCase):
    def setup(self):
        self.login = Login("Stella","Ngina","0726091999","sngina707@gmail.com,munie")
    def test_init(self):
        