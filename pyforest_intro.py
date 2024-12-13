import numpy as np
from pyforest import *
active_imports() #it displays the lib loaded to memory
lazy_imports() #to load all the lib frequently used in the data
a=np.zeros((2,2))
print(lazy_imports())
