from math import sqrt

##################################################   Q    U    I    Z   Z       W   I   N   E   R   S  ############################
### QUIZZ WINERS:
##  1ST PLACE: Teodora
##  2nd PLACE: Bogdan
##  3rd PLACE: Miha

def congrats(first, second, third, rest):
    print(f"{first} Congratulation, you are the first!")
    print(f"{second} Congratulation, you are the second!")
    print(f"{third} Congratulation, you are the third!")
    print(f"{rest} Keep trying to reach the top! You can do it! Practice, practice, practice!")

congrats("Teodora", "Bogdan", "Miha", "Everyone")


###############################################

# Access the 1st element from the element list with booleans

n = [1, 2, 3, ["ana", "mere", [True, False]]]
#    0  1  2         3 #  lista mare
#    0  1  2 |  0       1        2
#    0  1  2 |  0       1   |    0    1

#print(n[3][2][0])

## Access the the 2nd element from the list within the list

a = [1, 2, 3, [6, 9, 10]]
#print(a[3][1])

## Define the function i_love_math
## that returns "I love numbers" if a given number
## is > 100 and "I hate math" if the given number is < 100

def i_love_math(num):
    if num > 100:
        print("I love numbers")
    else:
        print("I hate math")

#i_love_math(50)

#### Create a mixed list (all 4 data types)
# with 5 elements read from keyboard.
# Iterate through list and add at the end of each element,
# letter "a". example("mama" --> "mamaa", "urat --> "urata")
# 3. Display the list.

#lst = input("Introduceti 5 cuvinte separate prin spatiu: ").split()
# new_l = []
# for item in lst:
#     item += "a"
#     new_l.append(item)
#print(new_l)

### functie de calcul a operatiilor mattematice cu 3 argumente

def mathOperations(a, b, operation):
    if operation == "+":
        return a + b
    elif operation == "-":
        return a - b
    elif operation == "*":
        return a * b
    elif operation == "/":
        return a / b
    elif operation == "radical":
        return sqrt(a) + sqrt(b)
    else:
        print("operations will not be made")


print(mathOperations(5, 7,"radical"))
print(mathOperations(5, 7, "+"))
print(mathOperations(5, 7, "-"))
print(mathOperations(5, 7, "*"))
print(mathOperations(5, 7, "/"))


