import numpy as np
import matplotlib.pyplot as plt
myarr=np.array([np.array([1,2,3,4,5,6]),np.array([8,7,6,5,4,6])],np.int64)
l11=[2015,2016,2017,2018,2019,2020,2021,2022,2023,2024]
l12=[10,11,10,15,17,12,20,18,19,23]
plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.plot(l11,l12,label="first" ,color="blue", linestyle="dashed", linewidth=5,marker="o",markersize=10,markerfacecolor="green")
plt.show()
#graph