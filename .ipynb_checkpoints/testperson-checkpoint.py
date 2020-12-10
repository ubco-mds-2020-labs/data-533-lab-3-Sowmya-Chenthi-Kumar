import unittest
import healthybreakfast.manual.Person as MP
import healthybreakfast.manual.Cereals as MC
import healthybreakfast.manual.Cereals1 as MC1
import pandas as pd

class TestMP(unittest.TestCase):
    # Define the setup method:
    def setUp(self):
        #d2=dd.Deficiency(25,1000,"Sowmya")
        #self.x1=d2.women()
        #self.x2=d2.men(23,2400,"Murali")
        print("Setup method")
        
    # Define the teardown method:
    def tearDown(self):
        print("Teardown method")
        
    # Define the setup class:
    @classmethod
    def setUpClass(cls):
        print("Setup class")
        
    # Define the teardown class:
    @classmethod
    def tearDownClass(cls):
        print("Teardown class")
        
    def test_diet(self):
        p = MP.diet()
        var = {"protein": 56,"cal": 2500,"fat":83, "sodium":2300, "fiber":38, "carbs":300,"potassium":3000}
        test = p.default_values("man","nutrient")
        #p.default_values()
        self.assertEqual(test['protein'],var['protein'])
        self.assertEqual(test['cal'],var['cal'])
        self.assertEqual(test['fat'],var['fat'])
        self.assertEqual(test['sodium'],var['sodium'])
        
    def test_manual_display(self):
        m = MP.manual_display("man", "protein")
        y = m.required_bar_graphs()
        
        z = y.patches
        
        self.assertEqual(z[0].get_height(), 56)
        self.assertEqual(z[1].get_height(), 2500)
        self.assertEqual(z[2].get_height(), 83)
        self.assertEqual(z[3].get_height(), 2300)
        
unittest.main(argv=[''], verbosity=2, exit=False)
        