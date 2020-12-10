import unittest
import pandas as pd
import pandas.testing
import healthybreakfast.find.Recommend as rmd

class TestRecommend(unittest.TestCase):
    
    # Define the setup class method:
    @classmethod
    def setUpClass(cls):
        print("Setup class method")
    # Define the teardown class method:
    @classmethod    
    def tearDownClass(cls):
        print("Teardown class method")
    
    # Define the required setup case:
    def setUp(self):
        print("Printing the setup statement")
        
    def tearDown(self):
        print("Printing Teardown statement")
        
    
    def test_recommend(self):
        #df1=pd.DataFrame({11:"Cheerios",64:"Special K",54: "Quaker Oatmeal"})
        self.assertEqual(rmd.recommend(5,1400),"Cheerios")
        self.assertEqual(rmd.recommend(1,400),"Special K")
        self.assertEqual(rmd.recommend(2,100),"Quaker Oatmeal")
        self.assertEqual(rmd.recommend(5,100),"Quaker Oatmeal")
        print("Done testing the recommend method")
        
    def test_mycereal(self):
        list_Special_k=[110, 6, 0, 230, 1.0, 16.0, 3, 55, 25, 53.131324]
        list_Cheerios=[110, 6, 2, 290, 2.0, 17.0, 1, 105, 25, 50.764999]
        list_Quaker=[100, 5, 2, 0, 2.7, 0.0, 0, 110, 0, 50.828392]
        list_Almond_delight=[110, 2, 2, 200, 1.0, 14.0, 8, 0, 25, 34.384843]
        
        # Creating test case for the first sample cereal:
        value_special_k=rmd.my_cereal("Special K")
        test_list_special_k=[]
        for elem in value_special_k.patches:
            test_list_special_k.append(elem.get_height())
        
        # Creating test case for the second samle cereal:
        value_Cheerios=rmd.my_cereal("Cheerios")
        test_list_Cheerios=[]
        for elem in value_Cheerios.patches:
            test_list_Cheerios.append(elem.get_height())
            
        # Creating test case for the third sample cereal:
        value_Quaker=rmd.my_cereal("Quaker Oatmeal")
        test_list_Quaker=[]
        for elem in value_Quaker.patches:
            test_list_Quaker.append(elem.get_height())
            
        # Creating test case for the fourth sample cereal:
        value_Almond=rmd.my_cereal("Almond Delight")
        test_list_Almond=[]
        for elem in value_Almond.patches:
            test_list_Almond.append(elem.get_height())
        
        
        self.assertListEqual(test_list_special_k,list_Special_k)
        self.assertListEqual(test_list_Cheerios,list_Cheerios)
        self.assertListEqual(test_list_Quaker,list_Quaker)
        self.assertListEqual(test_list_Almond,list_Almond_delight)
        print("Done testing the my_cereal method")

unittest.main(argv=[''],verbosity=2,exit=False)
