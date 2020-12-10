#### Second Assertion statements:
import healthybreakfast.find.Deficiency as dd
import unittest
def setUp_class(TestDeficiency):
    
    self.d2=dd.Deficiency(25,1455,"Sowmya")
    self.x1=self.d2.women()
    self.x2=self.d2.men(23,2400,"Murali")
        #print("Setup method")
    #self.d3=dd.Deficiency(56,2000,"Ana")
    #self.x3=self.d3.women()
    #self.x4=self.d3.men(45,6000,"Dave")
    
    
def tearDown_class(TestDeficiency):
    self.d2=None
    self.x1=None
    self.x2=None
        #print("Setup method")
    #self.d3=None
    #self.x3=None
    #self.x4=None
    
    
class TestDeficiency(unittest.TestCase):
    
    # Define the setup method:
    def setUp(self):
        self.d2=dd.Deficiency(25,1455,"Sowmya")
        self.x1=self.d2.women()
        self.x2=self.d2.men(23,2400,"Murali")
        #print("Setup method")
        self.d3=dd.Deficiency(56,2000,"Ana")
        self.x3=self.d3.women()
        self.x4=self.d3.men(45,6000,"Dave")
        
        
    # Define the teardown method:
    def tearDown(self):
        self.d2=None
        self.x1=None
        self.x2=None
        #print("Setup method")
        self.d3=None
        self.x3=None
        self.x4=None
        #print("Teardown method")
        
    # Define the setup class:
    #@classmethod
    #def setUpClass(cls):
       # print("Setup class")
        
    # Define the teardown class:
    #@classmethod
    #def tearDownClass(cls):
     #   print("Teardown class")
    
    def test_Diet(self):
        d=dd.Diet("Sowmya")
        self.assertEqual(d.default_values("man","p"),65)
        self.assertEqual(d.default_values("woman","p"),50)
        self.assertEqual(d.default_values("man","cal"),2900)
        self.assertEqual(d.default_values("woman","cal"),2000)
        
    def test_Deficiency1(self):
        self.assertEqual(self.d2.dif_p,-25)        
        self.assertEqual(self.d2.dif_p_m,42)
        
    def test_Deficiency2(self):
      
        x1_list=[1455,2000]
        x1_test_list=[]
        for elem in self.x1.patches:
            x1_test_list.append(elem.get_width())
            
        x2_list=[2400,2900]
        x2_test_list=[]
        for elem in self.x2.patches:
            x2_test_list.append(elem.get_width())
            
        x3_list=[]
        self.assertListEqual(x1_list,x1_test_list)
        self.assertListEqual(x2_list,x2_test_list)
        
        
unittest.main(argv=[''],verbosity=2,exit=False)