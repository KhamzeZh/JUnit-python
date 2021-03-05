import unittest
import Max_element
 
class Test(unittest.TestCase):
    def test_1(self):
        self.assertEqual(ma(q), 147)
        
    def test_2(self):
        self.assertEqual(ma(q), 150)
    def test_3(self):
        self.assertEqual(ma(q), 146)

    def test_4(self):
        self.assertEqual(ma(q), 148)
        
        
if __name__ == '__main__':
    unittest.main()
