import random as r
words=["hello","world","name","driver","mouse","keyboard","python"]
x=r.choice(words)
s=[]
stages = ['''
          
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']
stages=stages[::-1]
for i in range(len(x)):
    s.append("_")
c=0
while True:
    print(stages[c])
    if "_" in s and c==6:
        print("Hanged")
        break
    elif "_" not in s:
        print("Won")
        break
    for i in s:
        print(i,end=" ")
    print()
    t=input("enter the character: ")
    if t in x:
        for i in range(len(x)):
            if x[i]==t:
                s[i]=t
    else:
        c+=1