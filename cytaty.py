import random
with open('cytaty.txt', 'r') as cytat:
    wynik = cytat.readlines()
#for i in c:
    #print('*', i)
g = random.choice(wynik)
print('*****Twoja wiadomosc dnia***** '.center(100))
print(g.center(100))



