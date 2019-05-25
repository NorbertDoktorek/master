print("Program: Sprawdzamy dane uzytkownika")
def formularz():
    user = int(input("Ile danych chcesz wprowadzic: "))
    for i in range(user):
        imie = input("Imie: ")
        nazwisko = input("Nazwisko: ")
        miasto = input("Miasto: ")
        dane.append(imie)
        dane.append(nazwisko)
        dane.append(miasto)

dane = []

formularz()
#print("----------------------")

while True:
    print("Czy twoje dane sa poprawne? ", dane)
    test = input("T/N: ")
    if test.upper() == "T":
        break
    elif test.upper() == "N":
        dane = []
        formularz()


print("----------------------")
kolor = input("Podaj kolor: ")


while True:
    pesel = (input("Pesel: "))
    x = len(pesel)
    if x == 12:
        break

dane.append(kolor)
dane.append(pesel)
print("----------------------")
for element in dane:
    print(element)











