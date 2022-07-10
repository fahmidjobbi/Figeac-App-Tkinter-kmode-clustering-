#Loading the dataset
#Loading the dataset
import pandas as pd
read_file = pd.read_excel("/content/refdata.xlsx")
read_file.to_csv ("df.csv", index = None,header=True)
df = pd.read_csv("/content/df.csv")

######################################

df.groupby(['RefsPieces'])
df= df.drop(df.columns[1],axis=1)
df= df.drop(df.columns[1],axis=1)
df= df.drop(df.columns[2],axis=1)
df= df.drop(df.columns[2],axis=1)
df= df.drop(df.columns[2],axis=1)
df= df.drop(df.columns[2],axis=1)

from itertools import groupby

dict={}
from collections import OrderedDict, defaultdict
studentdict=df.to_dict('split')
#studentdict=studentdict.values()
s=studentdict['data']

list_of_lists = s
d={}
all_values = [list[0] for list in list_of_lists]
unique_values = set(all_values)

group_list = []
for value in unique_values:
  this_group = []
  for list in list_of_lists:
    if list[0] == value:
      this_group.append(list[1])
      d[list[0]]= this_group
  group_list.append(this_group)
  


dff=pd.DataFrame(d.items())
dff.to_csv ("datareg.csv", index = None,header=True)
datareg = pd.read_csv("/content/datareg.csv")
datareg = datareg.set_index('0')

datareg = datareg.replace('\[', '', regex=True)
datareg = datareg.replace('\]', '', regex=True)


datareg=datareg['1'].str.split(r",", expand=True)

datareg.to_excel("newwen.xlsx", index = True ,header=True)