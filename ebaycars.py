#First of all, We import the Numpy & Pandas libraries. Then, You maybe noticed that we used encoding Argument with 'pd.read_csv'; because it is decoded by "Latin-1".
#After that, We used DataFrame.info() and DataFrame.head() to undrastand more about our dataframe.
import pandas as pd
import numpy as np
auto=pd.read_csv('autos.csv',encoding='Latin-1')
auto
