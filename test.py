import joblib as joblib
import pandas as pd 
import numpy as np

cls=joblib.load('modeloo.sav')
dataclean=pd.read_csv("C:/Users/fahmi/Desktop/clustering model/dataclean.csv")
dataclean = dataclean.replace(np.nan,"", regex=True)
#predict dataclean with cls
clusters=cls.predict(dataclean)

dataclean.insert(0, "Cluster", clusters, True)

c0=dataclean[dataclean['Cluster']==0]
c0.to_excel("c0.xlsx", index = True ,header=True)


