# Import the required Packages information:
import pandas as pd

# Defining the parent class which has all the default nutritional values and some default display statements:
class Diet:
    import pandas as pd
    diet={}
    def __init__(self,name):
        self.name=name
        #self.age=age

    def default_values(self,gender,nutrient):
        diet={"man": {"p": 78,"cal": 9800},
               "woman": {"p": 89,"cal": 1600}}
        return diet[gender][nutrient]
    
    def display_values(self,name=0):
        if name==0:
            print("Hi!",self.name,"OOPS! Your nutrient levels are not up to the mark!")
            print("You are deficient by: \n")
            
        else:
            print("Hi",name,"OOPS! Your nutrient levels are not up to the mark!")
            print("You are deficient by: \n")
   
        
# Defining the child class as calculation the deficient values and giving a pictorical representation,
# for the deficient amount:

class Deficiency(Diet):
    import pandas as pd
    
    def __init__(self,w_protein=0,w_cal=0,w_name=0):
        Diet.__init__(self,w_name)
        self.w_name=w_name
        self.w_protein=w_protein
        self.w_cal=w_cal
        
    def women(self):
        dif_p=Diet.default_values(self,"woman","p") - self.w_protein
        dif_cal=Diet.default_values(self,"woman","cal") - self.w_cal
        
        if (dif_p<0 or dif_cal<0):
            Diet.display_values(self)
            df=pd.DataFrame({"your_protein_value": [self.w_protein],
                         "required_value":[Diet.default_values(self,"woman","p")]})
            #df.plot.barh(color={"your_protein_value":"red", "required_value":"green"},rot=0,align='center')
        else:
            print("Hey!!{} You are having all the required nutrient contents! Way to go!\n".format(self.w_name))
        
        
    def couple(self,m_protein,m_cal,m_name):
        if self.w_protein==0:
            Diet.display_values(self,m_name)
            self.deficiency_m(m_protein,m_cal,m_name)
        else:
            self.women()
            self.men(m_protein,m_cal,m_name)
                   

        
    def men(self,m_protein,m_cal,m_name):
        dif_p_m=Diet.default_values(self,"man","p") - m_protein
        dif_cal_m=Diet.default_values(self,"man","p")- m_cal
        if (dif_p_m<0 or dif_cal_m<0):
            Diet.display_values(self,m_name)
            df=pd.DataFrame({"your_protein_value": [m_protein],
                         "required_value":[Diet.default_values(self,"man","p")]})
            df.plot.barh(color={"your_protein_value":"red", "required_value":"green"},rot=0)
        else:
            print("Hey!! You have all the required nutrient contents! Way to go!")
        