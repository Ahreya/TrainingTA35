####### String Methods #######

### .capitalize()####
# modifica stringul astfel incat prima litera va fi mai mare si restul literelor vor fi mici
myStr = "casa mea este miCa"
print(myStr.capitalize())

### .endswith() ####
# verifica daca un string se termina cu litera data ca argument
# syntax: nume_str.endswith("something")
a = "my name is Diana"
print(a.endswith("is Diana"))

#### .find() ####
# cauta un substring si returneaza indexul unde se gaseste
# nu returneaza o eraoare daca ii dam un substring inexistent
# functioneaza numai cu stringuri
# syntax: nume_str.find("substring")

# find with one parameter
action = "Today I will learn python"
print(action.find("arn"))

# find with 2 parameters
# if you want to search the substring staring with a certain index
# syntax: nume_str("substring", poz)
dislike = "I don't wanna learn anything today"
print(dislike.find("anything", 21))

#### find with 3 parameters
# al treilea argument pointeaza catre indexul unde vrem sa terminam cautarea
# syntax: nume_string("substring", start_poz, end_poz)
love = "castane"
########0123456
print("Substringul 's' se gaseste pe pozitia:", love.find("s",1,3))

#### .isalnum() #####
# verifica daca un string contine numai litere si cifre. Returneaza un bool --> True/False
mother = "Cristina10"
father = "Ioan Ciubotaru"
print("mother: ", mother.isalnum())
print("father: ", father.isalnum())

#### .isalpha() #####
# verifica daca un string este format numai din litere si returneaza True/False
#syntax: nume_str.isaplha()
#spatiile nu sunt considerate litere, sunt considerate caractere

a_str = "Am pescarusi"
b_str = "elefant"
print("a_str: ", a_str.isalpha())
print("b_str", b_str.isalpha())

#### isdigit() ####
# verifica daca un string este format numai din numere
# syntax: nume_str.isdigit()
age = "2"
age2 = "mama5444"

print("age ", age.isdigit())
print("age2", age2.isdigit())
print(age.isnumeric())

###### islower() #####
# verifica daca un string este format numai din litere mici si returneaza True/False
# syntax: nume_str.islower()
small_letter = "am plecat in vacanta"
print("small_letter", small_letter.islower())

#### .isspace() ####
# verifica daca stringul este format numai din spatii goale si returneaza True/False
#syntax nume_str.isspace()
spatiu = "am plecat"
spatiu2= "    "
print("spatiu", spatiu.isspace())
print("spatiu2", spatiu2.isspace())

#### .isupper() ####
# verifica daca un string este format numai din litere mari si returneaza True/False
# syntax: nume_str.isupper()
mama = "CASA"
print("mama", mama.isupper())

###### .lower() ####
# inlocuieste toate literele mari din string cu litere mici
#syntx: str.lower()
mama = "CASA"
print("mama", mama.lower())

#### .upper() ####
# inlocuieste toate literele mici ale stringului cu litere mari
# syntax: nume_str.upper()
home = "here"
print("home", home.upper())

##### replace()####
# returneaza o copie a stringului original in care toate aparitiile primului argument au fost inlocuite cu al doilea argument
# syntax: nume_str.replace(string_to_replace, replace)
action2 = "cainele meu e mic si rau si ma musca"
print(action2.replace("cainele", home.upper()))

# ex
s = "It is either easy or impossible"
s = s.replace('easy', 'hard')
print(s)

s = "It is either easy or impossible"
s = s.replace('i', 'n')
print(s)

#### .strip() ###
# returneaza un string fara leading space
#syntax: str.strip()
n ="mama are"
l = "  mama are"
print(n)
print(n.strip())
print(l)
print(l.strip())

### split() ####
# aceasta metoda considera ca stringurile sunt delimitate de spatii albe
# syntax: str.split()
ex = "bujori trandafiri crini"
print(ex.split())

### exercitiu
# myvar  = input("Introduceti 4 cuvinte separate prin spatiu: ") # ana are multe mere
# x, y, z, w = myvar.split()
# print(x)
# print(y)
# print(z)
# print(w)

##### swapcase() ####
# returneaza un nou string in care tipul de litere este inversat. litere mici --> litere mari, viceversa
s = "i WaS a BAD cat"
print(s.swapcase())



