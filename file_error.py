#SyntaxError: (unicode error) 'unicodeescape' codec can't decode bytes 
# in position 2-3: truncated \UXXXXXXXX escape
#C:\Users\Documents\cars.csv',

import pandas as pd

#To avoid error as the output,m kindly put r at the beginning of your file directory
cars = pd.read_csv(r'C:\Users\Documents\cars.csv', index_col=0)

#You can also add another back slash to it as the 2nd method to avoid this error
#cars = pd.read_csv('C:\\Users\\Documents\\cars.csv', index_col=0)

print(cars)