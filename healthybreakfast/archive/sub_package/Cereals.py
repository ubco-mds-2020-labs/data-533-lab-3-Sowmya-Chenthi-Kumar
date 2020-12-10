## Cereals.py

import pandas as pd
import pygal
from IPython.display import SVG, display
from pygal.style import Style 

class Cereals_nutrition:
    def display_Cereals(self):
        data = pd.read_excel("cereal.xlsx", sheet_name='Modified_Cereal', index_col=0)
        bar_chart = pygal.HorizontalStackedBar() 
        bar_chart.title = "Nutrient composition of cereals"
        bar_chart.add('protein', data['protein'] ) 
        bar_chart.add('calories (X100)', data['calories']/100) 
        bar_chart.add('fat', data['fat'])
        bar_chart.add('sodium (X100)', data['sodium']/100 )
        bar_chart.add('fiber', data['fiber'])
        bar_chart.add('carbohydrates', data['carbo'])
        bar_chart.add('sugar', data['sugars'])
        bar_chart.add('potassium (X100)', data['potass']/100)
        bar_chart.add('vitamins (X10)', data['vitamins']/10)


        bar_chart.render_to_file('HorizontalStackedBar.svg')
        display(SVG(bar_chart.render (disable_xml_declaration=True)))

class deficiency_nutrition:
    def display_worldmap(self):
        custom_style = Style( colors = ('#FF0000' , '#0000FF' , '#00FF00' , '#000000', '#FFD700')) 
        worldmap =  pygal.maps.world.World(style = custom_style) 
        worldmap.title = "Nutrient deficient countries"
        worldmap.add('Protein deficient', ['in', 'br', 'sa'])
        worldmap.add('Calories deficient',['so', 'tg', 'mw'])
        worldmap.add('vitamin deficient', ['ke', 'ml', 'ng', 'sd', 'ao'])
        worldmap.add('sodium deficient', ['ph', 'eg', 'gh'])
        worldmap.add('iron deficient', ['ye','za', 'pk'])
        worldmap.render_to_file('nutrient.svg')
        display(SVG(worldmap.render (disable_xml_declaration=True))) 
         