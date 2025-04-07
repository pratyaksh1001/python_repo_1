import random
cards={
    "spades":['1','2','3','4','6','7','8','9','10','J','Q','K','A'],
    "diamond":['1','2','3','4','6','7','8','9','10','J','Q','K','A'],
    "heart":['1','2','3','4','6','7','8','9','10','J','Q','K','A'],
    "club":['1','2','3','4','6','7','8','9','10','J','Q','K','A']
}
total=[11,2,3,4,5,6,7,8,9,10,10,10,10]
random.shuffle(total)
player=0
dealer=0
winner=""
c=0
while True:
    print(player)
    x=input("enter yes to withdraw card: ")
    if x=='yes':
        player+=total[c]
        c+=1
    else:
        break
while True:
    if dealer<16:
        dealer+=total[c]
        c+=1
    elif dealer>16:
        break
print("player:",player)
print("dealer:",dealer)
if 21-player<21-dealer:
    if player<22:
        winner="player"
    else:
        winner="dealer"
else:
    if dealer<22:
        winner="dealer"
    else:
        winner="player"
print("winner is:",winner)