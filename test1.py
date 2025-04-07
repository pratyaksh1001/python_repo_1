#   matrix sum
l1=[[1,2,3],[4,5,6],[6,7,8]]
l2=[[6,8,9],[4,3,2],[4,8,3]]
l3=[[],[],[]]
for i in range(0,3):
     for j in range(0,3):
          l3[i].append(l1[i][j]+l2[i][j])
for x in l3:
     print(x)