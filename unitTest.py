import unittest
import mainApp as app

class TestMyApp(unittest.TestCase):
    
    def setUp(self):
        self.app = app
    
    def test_show(self):
        lst = ["Test1", "Test2"]
        self.assertEqual(app.func2(lst, "Test3"), ["Test1", "Test2", "Test3"])

if __name__ == '__main__':
    unittest.main()