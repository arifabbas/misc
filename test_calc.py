import unittest
from calc import Calc

class TestCalc(unittest.TestCase):
    def test_add(self):
        tc1=Calc(1,1)
        tc2=Calc(1,-1)
        tc3=Calc(-1,-1)
        self.assertEqual(tc1.add(1,1),2)
        self.assertEqual(tc2.add(1,-1),0)
        self.assertEqual(tc3.add(-1,-1),-2)

    def test_sub(self):
        tc1=Calc(1,1)
        tc2=Calc(1,-1)
        tc3=Calc(-1,-1)
        self.assertEqual(tc1.sub(1,1),0)
        self.assertEqual(tc2.sub(1,-1),2)
        self.assertEqual(tc3.sub(-1,-1),0)

    def test_mul(self):
        tc1=Calc(1,1)
        tc2=Calc(1,-1)
        tc3=Calc(-1,-1)
        self.assertEqual(tc1.mul(1,1),1)
        self.assertEqual(tc2.mul(1,-1),-1)
        self.assertEqual(tc3.mul(-1,-1),1)

    def test_div(self):
        tc1=Calc(1,1)
        tc2=Calc(1,-1)
        tc3=Calc(-1,-1)
        tc4=Calc(1,0)
        self.assertEqual(tc1.div(1,1),1)
        self.assertEqual(tc2.div(1,-1),-1)
        self.assertEqual(tc3.div(-1,-1),1)
        with self.assertRaises(ZeroDivisionError):
            tc4.div(1,0)

    def setUp(self):
        print('Setup func')
    
    def tearDown(self):
        print('tear Down func')
    
    @classmethod
    def setUpClass(cls):
        print('Setup Class')
    
    @classmethod
    def tearDownClass(cls):
        print('tearDownClass')

if __name__=='__main__':
    unittest.main()