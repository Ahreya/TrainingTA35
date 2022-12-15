### None
# vaerificam daca o variabila este None sau nu este None cu
# is None, is not None, NU FOLOSIM ==

### cum se face unpacking ####
# vrem sa facem unpcking la o colectie de date si sa asignam fiecare valoare unei variabile
# tup = (1, 2, 3, 4)
# a, b, c, d = tup
# print(a)
# print(b)
# print(c)
# print(d)
# poti face asta cu orice colectie

# unpack dictionary
# dic = {"a": 1, "b": 2, "c": 3}
#
# # get keys
# e, f, g = dic
#print(f"e: {e}, f: {f}, g: {g}")

# get tuples of key, value
#e, f, g = dic.items()
#print(f"e: {e}, f: {f}, g: {g}")

# get only values
# e, f, g = dic.values()
# print(f"e: {e}, f: {f}, g: {g}")

##### Multiple assignement - switch values ###
x, y = 5, 10

# alt limbaj
# temp_var = x
# x = y
# y = temp_var

### in python
x, y = y, x
print(x, y)

#### ternar condition #####

if 10 > 5:
    x = 2
else:
    x = 0

x = 2 if 10 > 5 else 0


########

even_num = []
odd_num = []
poz_num = []
neg_num =[]

# for num in numbers:
#     if num % 2 ==0:
#         even_num.append(num)
#     else:
#         odd_num.append(num)
#     if num >= 0:
#         poz_num.append(num)
#     else:
#         neg_num.append(num)
#
# print(f"numere_pare {even_num}")
# print(f"numere_impare {odd_num}")
# print(f"numere_poz {poz_num}")
# print(f"numere_neg {neg_num}")

######## elif ######

numbers = [1, 5, -5, 0, 3, -2, 6, 10]

for num in numbers:
    if num % 2 == 0:
        even_num.append(num)
    elif num % 2 != 0:
        odd_num.append(num)
    elif num >= 0:
        poz_num.append(num)
    else:
        neg_num.append(num)

print(f"numere_pare {even_num}")
print(f"numere_impare {odd_num}")
print(f"numere_poz {poz_num}")
print(f"numere_neg {neg_num}")
