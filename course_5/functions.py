#### Turn this snipet into a function
#
print("Enter a value: ")
a = int(input())

print("Enter a value: ")
b = int(input())

print("Enter a value: ")
c = int(input())

### define the function

def get_value():
    print("Enter a value: ")

print("We start here")
get_value()
print("We end here")

####### positional parameter passing

def introduction(first_name, last_name):
    print("Hello, my name is ", first_name, last_name)

# apelam functia
introduction("Luke", "Skywalker")
introduction("Clark", "Kent")
introduction("Jessie", "J")

introduction(first_name="James", last_name="Bond")
introduction(last_name="Cat", first_name="Woman")

### functie cu parametru predefinit
def introduction_a(first_name, last_name = "Smith"):
    print("Hello, my name is", first_name, last_name)

introduction_a("Diana")
introduction_a("Laura", "Noris")

#### return fara argumente ####
# happy new year whishes

def happy_new_year(whishes = True):
    print("Three...")
    print("Two...")
    print("One...")
    if not whishes:
        return
    print("Happy new year")

# apelam functia cu whishes True
happy_new_year()

# apelam functia cu whishes False
happy_new_year(False)
print("I am here!!!!!")

#### functie cu un argument gresit


def introduction_b(first_name, last_name):
    print("Hello, my name is ", first_name, last_name)


introduction_b("Luke")



#### functie cu mai multe argumente decat parametrii

def introduction_c(first_name, last_name):
    print("Hello, my name is ", first_name, last_name)


introduction_c("Luke", "Mina", "Dungeon")

#### return cu argumente - used

def boring_function():
    a = 345
    return a

x = boring_function()
print("The boring_function has returned its results. It's: ", x)

### retrun - we will not use what it returns


def boring_function_a():
    print("'Boredom Mode' ON.")
    return 123


print("This is quite interesting!")
a = boring_function_a() + 342
print(a)
print("This lesson is boring ...")
print(boring_function_a() + 243)


#### invocam functie cu lista ##
# suma elemntelor din lista

def list_sum(my_list):
    sum = 0

    for num in my_list:
        c = 12
        sum += num + c
    return sum


print("Suma elementelor din lista este: ", list_sum([1, 5, 8, 3]))

#### use function in function
# create a function that returns the sum of 2 numbers multiplicated with the sum from previous function
# return the new value


def multiplication(num1, num2, list):
    sum_num = num1 + num2
    return sum_num * list_sum(list)


print(multiplication(3, 8, [1, 3, 5]))



#### function that returns a list ##########

def my_sweet_list(n):
    sweet_list = []

    for i in range(n):
        sweet_list.insert(0, i)

    return sweet_list[::-1]


print(my_sweet_list(5))

###### functie --> valoarea absoluta a unui numar

def absolute_value(num):
    """
    This function returns the absolute value of the entered number
    :param num: the number
    :return: absolute value
    """
    if num >= 0:
        return num
    else:
        return -num



################ T E M A #######################
# sa se introduca de la tastatura un numar si sa se afle valoarea absoluta
# utilizatorul va introduce ceva daca vrea sa termine "jocul".
while True:
    num_user = int(input("Introdu un numar. Daca vrei sa te opresti baga 0: "))
    if num_user == 0:
        break
    else:
        print(absolute_value(int(input("Introduceti un numar: "))))


print(absolute_value(int(input("Introduceti un numar: "))))

