####### LISTE #######

# Lista goala
myList = []
print(myList)

# Lista cu elemente mixte

lst = ["mama", 13, True, 13.5, True, False, "miau"]
print(lst)

# de cate ori apare True in lista
print(lst.count(True))

# aflam elementul de pe pozitia 2
print(lst[2])

##### append ###
ls1 = [1, 2, 3, 4]
ls2 = ['n', 'm', 0, True]
# adaugam lista 2 la lista 1

ls1.append(ls2)
print(ls1)

# copiem un elementul de pe poz 1 din lista 2
# adaugam la lista 1
elem = ls2[1]
print(elem)
ls2.remove(elem)
print(ls2)
ls1.append(elem)

print("Lungimea listei ls 2 este ",len(ls1))
print(ls1)

## extend
print("Lista 1 este: ", ls1)
print("Lista 1 este: ", ls2)
ls1.extend(ls2)
print("Noua ls1 este: ",ls1)
print("Lungimea ls1 este: ",len(ls1))

# inlocuim un element din lista
ls1[4] = "new_val"
print("LS1 = ", ls1)

###### tuple ###

#cream o tupla cu string-uri
myT = ("unu", "doi", "trei")
print(type(myT))

# vrem sa aflam elementul de pe pozitia 0
print("Elementul de pe pozitia 0 din tupla myT: ",myT[0])

# verificam daca elementul "trei" este in tupla
print("trei" in myT)

# vrem sa inlocuim elementul de pe pozitia 1
# myT[1] = 7

# avem o lista. sa se afle elementul de pe pozitia 1.
# sa se inlocuiasca elementul de pe pozitia 1 cu "bingo".
# daca elementul de pe pozitia 1(vechi) este in lista, atunci vom afisa "I am here",
# daca nu se afla in lista, afisam "We got rid of it"

lista = ["oua", "zahar", 7]
print(lista[1])
elem = lista[1]
lista[1] = "bingo"
print(lista)

if elem in lista:
    print("I am here")
else:
    print("I got rid of it")

### tupla def2
a = 1,2,3,4,5
print(type(a))

###### seturi #####

myset = {"iarna", "primavara", "vara", "toamna"}

#afisam lungimea setului
print(len(myset))

# add elements to the set

myset.add("frig")
myset.add("cald")
myset.add(("elem1", "elem2"))
print("Setul are urm valori: ", myset)

# remove element tupla
myset.remove(("elem1", "elem2"))
print("Myset: ", myset)
# remove an element that doesn't exist
#myset.remove("calda")

### discard

myset.discard("frig")
print(" ////////////", myset)
myset.discard("noapte")

#asignam o alta valoare elementului de pe poz 0 --> nu se poate
myset[0]="True"

######## dictionare #####

dict1 = {"a": 2, "b": 3, "c": 5}

# afisam vaoarea lui b
print("Val cheii b: ", dict1["b"])

dt = {"tip_carte" : "roman", "editura" : "Corint",
      "Autor": "Agatha Christie", "nr_pg":250,
      "carti": ["Cu cartile pe fata", "Oglinda", "Crima din Orien Expres"]}

#din cheia carti vrem sa obtinem a doua carte
print(dt["carti"][1])

######### avem lista in lista, cum accesam valorile din lista care este in lista

a = [1,2, "sapte", [3, 6, 0]]
print(a[3][0])
