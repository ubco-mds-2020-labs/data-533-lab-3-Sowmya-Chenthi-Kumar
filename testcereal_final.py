import unittest
import healthybreakfast.manual.Person as MP
import healthybreakfast.manual.Cereals as MC
import healthybreakfast.manual.Cereals1 as MC1
import pandas as pd

def setUp_Class(TestMC1):
    self.c = MC1.Cereals_nutrition1()
    self.x = self.c.display_Cereals1()    
    self.nutrients= self.x.patches
    self.calories = self.nutrients[:74]
    self.protein = self.nutrients[74:2*74]
    self.fat = self.nutrients[2*74:3*74]
    self.sodium = self.nutrients[3*74:4*74]    
            
def tearDown_Class(TestMC1):
    self.c = None
    self.x = None 
    self.nutrients= None
    self.calories = None
    self.protein = None
    self.fat = None
    self.sodium = None

data = pd.read_excel("cereal.xlsx", sheet_name='Modified_Cereal', index_col=0)

class TestMC1(unittest.TestCase):
    
    def setUp(self):
        self.c = MC1.Cereals_nutrition1()
        self.x = self.c.display_Cereals1()   
        self.nutrients= self.x.patches
        self.calories = self.nutrients[:74]
        self.protein = self.nutrients[74:2*74]
        self.fat = self.nutrients[2*74:3*74]
        self.sodium = self.nutrients[3*74:4*74]    
               
    def tearDown(self):
        self.c = None
        self.x = None 
        self.nutrients= None
        self.calories = None
        self.protein = None
        self.fat = None
        self.sodium = None
            
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
        