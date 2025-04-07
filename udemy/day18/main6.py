import colorgram as cg
colors=cg.extract("Screenshot(158).png",50)
c=[]
for i in colors:
    r=i.rgb.r
    g=i.rgb.g
    b=i.rgb.b
    c.append((r,g,b))
for i in c:
    print(i)