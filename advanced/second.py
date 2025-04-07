import numpy as np
import matplotlib.pyplot as plt

lx=[2015,2016,2017,2018,2019,2020,2021,2022,2023,2024]
ly=[10,11,10,15,17,12,20,18,19,23]
plt.xlabel("year")
plt.ylabel("profit")
plt.bar(lx,ly,width=0.8,color=['red','green'])
plt.show()