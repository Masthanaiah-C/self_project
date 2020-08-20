import unittest
import rand

class check(unittest.TestCase):
    def cls1(self):
        obj1=rand.gen()
        self.assertIn(obj1.com_choice(),[1,2,3])
        self.assertNotIn(obj1.com_choice(),list(range(-1000,1)))
        self.assertNotIn(obj1.com_choice(),list(range(4,1000,1)))
    def cls2(self):
        obj2=rand.comp()
        self.assertEqual(obj2.result("rock","scissors"),[1,0])
        self.assertEqual(obj2.result("scissors","paper"),[1,0])
        self.assertEqual(obj2.result("paper","rock"),[1,0])
        self.assertEqual(obj2.result("rock","paper"),[0,1])
        self.assertEqual(obj2.result("paper","scissors"),[0,1])
        self.assertEqual(obj2.result("scissors","rock"),[0,1])
        self.assertEqual(obj2.result("rock","rock"),[0,0])
        self.assertEqual(obj2.result("scissors","scissors"),[0,0])
        self.assertEqual(obj2.result("paper","paper"),[0,0])
    def cl3(self):
        self.assertGreaterEqual(5,5)
if __name__=="__main__":
    unittest.main()
        

        
