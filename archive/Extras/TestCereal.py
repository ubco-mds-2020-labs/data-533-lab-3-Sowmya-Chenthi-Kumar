import unittest
import healthybreakfast.manual.Person as MP
import healthybreakfast.manual.Cereals as MC
import healthybreakfast.manual.Cereals1 as MC1
import pandas as pd

data = pd.read_excel("cereal.xlsx", sheet_name='Modified_Cereal', index_col=0)

class TestMC1(unittest.TestCase):
    
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
    
    def test_display_Cereals1(self):
        c = MC1.Cereals_nutrition1()
        x = c.display_Cereals1()
        
        nutrients= x.patches

        calories = nutrients[:74]
        protein = nutrients[74:2*74]
        fat = nutrients[2*74:3*74]
        sodium = nutrients[3*74:4*74]
        
        self.assertEqual(calories[0].get_width(), data.iloc[0,0])
        self.assertEqual(calories[1].get_width(), data.iloc[1,0])
        self.assertEqual(protein[0].get_width(), data.iloc[0,1])
        self.assertEqual(protein[1].get_width(), data.iloc[1,1])
        
        
    def test_display_worldmap(self):
        d = MC.deficiency_nutrition()
        d.display_worldmap()
        self.assertEqual(d.worldmap.title, "Nutrient deficient countries")    
        
unittest.main(argv=[''], verbosity=2, exit=False)