import math
cash=input("How much you got?")
Yellow=int(cash)/1000
yellow=math.floor(Yellow)
print("Yellow chips",yellow)
Purple=(int(cash)-yellow*1000)
purple=math.floor(Purple/500)
print("Purple chips",purple)
Black=math.floor((int(cash)-purple*500-yellow*1000)/100)
print("Black chips",Black)
Blue=math.floor((int(cash)-Black*100-purple*500-yellow*1000)/50)
print("Blue chips",Blue)
Green=math.floor((int(cash)-Blue*50-Black*100-purple*500-yellow*1000)/25)
print("Green chips",Green)
Red=math.floor((int(cash)-Green*25-Blue*50-Black*100-purple*500-yellow*1000)/5)
print("Red chips",Red)
White=math.floor((int(cash)-Red*5-Green*25-Blue*50-Black*100-purple*500-yellow*1000)/1)
print("White chips",White )





