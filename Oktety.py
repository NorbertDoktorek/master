import random
from tkinter import *
id

window = Tk()
window.geometry("480x360")
window.title('Oktety_adresów_IP')
window.configure(background='pink')
window.resizable(0, 0)


def klasa_A():
    print("Klasa A: ", random.randrange(126),".",random.randrange(1),".",random.randrange(1),".",random.randrange(1))

button1 = Button(window, text="Klasa A", command=klasa_A)
button1.pack()

def klasa_B():
    print("Klasa B: ", random.randrange(128, 191),".",random.randrange(1, 254),".",random.randrange(1),".",random.randrange(1))


button2 = Button(window, text="Klasa B", command=klasa_B)
button2.pack()

def klasa_C():
    print("Klasa C: ", random.randrange(192, 223),".",random.randrange(1, 255),".",random.randrange(2,254),".",random.randrange(1))


button3 = Button(window, text="Klasa C", command=klasa_C)
button3.pack()


window.mainloop()
