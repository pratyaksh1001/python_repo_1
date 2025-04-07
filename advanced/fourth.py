import numpy as np

arr1=np.array([[7,3,4],[7,8,9],[4,2,5]])
l2=[]
for i in range(3):
    l2.append(arr1[:,i])
arr2=np.array(l2)
print(arr2)

#code to find the transpose of a matrix