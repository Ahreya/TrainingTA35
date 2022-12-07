import time

############ while ########
### endless loop
# endless loop happens when the condition is always true and the loop body doesn't modify the condition
#ex 1

# while True:
#     print("I am stuck inside a loop")

#ex2

while True:
    print("I am stuck here, Help!")
else:
    print("something")


#ex3
# write a program that reads a sequence of numbers
# and counts how many numbers are even and how many are odd
# the program terminates when zero is entered

# What we need?
# var - odd numbers
# var - even numbers

# read the number first
odd_numbers = 0
even_numbers = 0
number = int(input("Enter a number or type 0 to stop: "))

# 0 terminates the execution
while number != 0:
    # check if the number is even
    if number % 2 == 0:
        even_numbers += 1
    else:
        # increase the odd numbers
        odd_numbers += 1
    number = int(input("Enter a number or type 0 to stop: "))


print("Too bad, user entered 0!")
print("Odd numbers count: ", odd_numbers)
print("Even numbers count: ", even_numbers)

#### ex 4
# make a counter that counts the last 10 seconds until new year
# after the last second, print "Happy new year!"

# De ce avem nevoie?
# o variabila counter

counter = 10
while counter != 0:
    print(counter, "seconds left")
    #se scade o secunda
    counter -= 1
    time.sleep(1)
print("Happy new year!!!!", counter)

########### for ##############
# ex 1
# write a for loop that counts to five
# body of the loop - print the loop iteration number and the word "Mississippi"
# use time.sleep(1)
# write a print function with the final message

for second in range(1, 6):
    print(second, "Mississippi")
    time.sleep(1)
print("I will search you and I'll find you!")

## ex 2
# Define a new list with 7 elements
# We want to calculate the sum of all numbers inside the list

#Ce avem nevoie?
# o lista, o var sum
# my_list = [2, 10, 15, 15, 3, 5, 20]
# sum = 0 # we start with a counter that we initialize with 0 (we haven't added any number yet)

for i in my_list:
    print(f"Adding {i} to {sum}")
    sum += i # as long as we haven't reached the end of the list we will add the current elem to the previous total
    print(f"Current sum is {sum}")
else:
    print("We are done with the sum")

print(f"The sum of the elements in the list is: {sum}")

##### break ####
print("The break instruction ")
for i in range (3, 8):
    if i == 4:
        break
    print("Inside the loop ", i)
print("Outside the loop")

###### continue ######
print("The continue instruction ")
for i in range (3, 8):
    if i == 4:
        continue
    print("Inside the loop ", i)
print("Outside the loop")

### for each ####
#
# avem o lista cu 6 animale
# parcurgem lista cu cele 6 animale si printam "I love this animal"

animals = ["zebra", "tigru", "maimuta", "iepure", "pantera", "panda"]

for animal in animals[::-1]:
    print(f"I love this animal --> {animal}")

############# temaaaaaaaaa #### incercati si pe alte structuri de date

# a junior magician has picked a secret number
# he has hide it in a variable named secret_number
# he wants everyone to run his program to play Guess the secret number
# if the user doesn't guess the number, he will be stuck in the loop
# if he guessed the number, then the magician will let him out

secret_number = 23

print("======= Welcome to my game silly human! =========")
user_nr = int(input("Enter a number between 0 and 30: "))

while user_nr != secret_number:
    print("You are stuck in my loop, ha ha ha, you are mine forever!!!")
    user_nr = int(input("Enter the number again: "))
print(secret_number, "Well done human! You are unfortunately free now!")
