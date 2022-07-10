#Loading the dataset
import pandas as pd
import numpy as np
from kmodes.kmodes import KModes
import matplotlib.pyplot as plt
dataclean = pd.read_excel("C:/Users/fahmi/Desktop/OutilsProject/cleandata.xlsx")
dataclean.to_csv ("dataclean.csv", index = None,header=True)
dataclean = pd.read_csv("C:/Users/fahmi/Desktop/clustering model/dataclean.csv")
dataclean = dataclean.replace(np.nan,"", regex=True)




# Building the model with 4 clusters
kmode = KModes(n_clusters=4, init = "random", n_init = 5, verbose=1)
kmode.fit_predict(dataclean)








import joblib 
filename='modeloo.sav'  
joblib.dump(kmode, filename) 

