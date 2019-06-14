lista = {
    "dom" : ["szkola", "kosciol", "bar"],
    "szkola" : ["dom", "szpital"],
    "kosciol" : ["dom", "bar", "kino"],
    "bar" : ["dom", "kosciol", "szpital"],
    "szpital" : ["szkola", "bar", "kino", "teatr"],
    "kino" : ["kosciol", "szpital", "teatr"],
    "teatr" : ["szpital", "kino"]
}
for key,val in lista.items():
    for v in val:
        print(key,"----", v)




#print(lista["dom"])