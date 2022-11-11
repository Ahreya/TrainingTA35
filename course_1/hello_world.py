############## COMENTARII ##################

# acesta este un comentariu
# acesta este un alt comentariu

"""
acesta
este un
comentariu pe mai multe
linii
"""

######### Functia print() #############
#syntax: print(something)
# functia print afiseaza ceva in consola

print("Hello world")
print('Hello world')
print("lalalla")

# print something with with new line. the chaacter we use is "\n"
print("Hello world/nI am Marcus") #-> it will print:
# Hello World
# I am Marcus

############## Variabile si tipuri de date  ###############
a = 5 # int
b = 6 # int
c = 20 # int
d = "mama" #string
imi_place_zaharul = True # bool
i_have_hope = False
pret = 125.50
ENVIRONMENT = "MacOS" #constanta

# variabile tip string
culoare = "verde"
nume = "Ion"
varsta = "25"
print(varsta)
print(culoare)
print(nume)


############# Functia type()############
#syntaxa: type(argument)
#afiseaza tipul unei variabile

name = "Marina"
price = 35.99
age = 20
hate_mangos = True

print(type(name))
print(type(hate_mangos))
print(type(price))
print(type(age))

############### type casting  ###############
# we use for casting the following: int(), float(), str(), bool()
# syntax cast_func(variabila)

s = 25 #int
s = str(s) # convertim variabila s in string
print("s After conversion:")
print(type(s))

n = 27
n = 50 # override
print(n)
print(type(str(85)))
c = 20
c = str(c) # override 


############ print cu formatare si concatenare  ##############
# are syntaxa print(f"something{var}")

fructe = "mere, pere, gutui"
legume = "morcovi, telina"
concat_string = fructe + " " + legume
print(concat_string)
print(fructe + " " + legume)
pret = 10
print(fructe + " " + legume + " la " + str(pret) + " lei")

#print cu formatare
print(f"Azi am cumparat {fructe}, {legume}, toate la {pret} lei")

name = "Maria"
parent = "mama"
age = 46

# mama mea este Maria si are 46 de ani


print(f"{parent} mea este {name} si are {age} de ani")

#### assert ####
invat_Python_acum = False
assert invat_Python_acum == True, "Trebuia sa fiu la curs, dar nu sunt"
print("Sunt la curs")

imi_place_prajitura = True
assert imi_place_prajitura == False, "doar unele prajituri"
print("cele de casa")

nu_mi_place_sa_zbor = True
assert nu_mi_place_sa_zbor == True, "merg in Cipru"
print("merg cu masina")


############ functia input() ###########

name = input("Introduceti numele de familie: ")
surname = input("Introduceti prenumele: ")
print(f"Numele meu este {name} {surname}")

# type casting - int -ex 1
number = input("Introduceti un numar intreg: ")
print(type(int(number)))

#type casting - int - ex 2
number2 = int(input("Introduceti un numar intreg: "))

############## metode string #############

myString = "Astazi am invatat multe la python"
myString2 = "mere"

#printam lungimea stringului
print(len(myString2))
print(len(myString))

string3 = "diamant"
# d i a m a n t e l e
# 0 1 2 3 4 5 6 7 8 9

# vrem sa obtinem dia
new_str = string3[:3]
print(new_str)

# vrem sa obtinem ant
new_str2 = string3[4:]
print(new_str2)

# vrem sa obtinemant
new_str3 = string3[4:7]
print(new_str3)





















