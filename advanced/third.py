import numpy as np
import matplotlib.pyplot as plt
import random as rn

year=np.array([2019,2020,2021,2022,2023])
l=[]
for i in range(5):
    l.append(rn.randrange(100,200))
data=np.array(l)
data[-1]=1000
plt.pie(data,colors = ("orange", "cyan", "brown",
          "grey", "indigo", "beige"),labels=year)
plt.show()