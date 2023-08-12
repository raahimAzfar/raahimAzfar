# Imports Pandas and abbreviates it as pd.
import pandas as pd

# My first DataFrame
fruit_sales = pd.DataFrame({'Apples': [35, 41], 'Bananas': [21, 34]}, index = ['2017 Sales', '2018 Sales'])

fruit_sales

# My first series
ingredients = pd.Series(['4 cups', '1 cup', '2 large', '1 can'],
                        index = ['Flour', 'Milk', 'Eggs', 'Spam'],
                       name = 'Dinner')

ingredients