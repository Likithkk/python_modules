# from google.colab import drive
# drive.mount(' path eg:/content/drive ')
file_name = " path of file "
# import os
# print("size of file is {}MB".format(os.path.getsize(file_name)>>20))

import time
import numpy as np
import pandas as pd
import datatable as dt

# read time comparision
s=time.time()
df_panda = pd.read_csv(file_name)
e = time.time()
pd_time =e-s
print("Pandas loading time is {}",format(pd_time))
df_panda.sort_values(by = 'col_name')


# for datatable
df_datatable = dt.fread(file_name)
# to convert datatable to pandas
df_convert_pandas = df_datatable.to_pandas()
#to sort 
df_datatable.sort('col name')
