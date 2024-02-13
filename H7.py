
#7.2

print("\n 7.2 \n")

people = int(input("How many people are dining with you? "))

if people > 8:
    print("You'll have to wait for a table. ")

else:
    print("Your table is ready!")

#7.3

print("\n 7.3 \n")

number = int(input("Give a number:"))

if number % 10 == 0:
    print(number, "is a multiple of 10.")
else:
    print(number, "is not a multiple of 10.")

# 7.4

print("\n 7.4 \n")

active = True

while active == True:
    topping = input("What'd you like on your pizza?")
    if topping == 'quit':
        print("Bye bye!")
        break
    else:
        print("Great! I'll add ", topping, " on your pizza!")

# 7.5

print("\n 7.5 \n")

active = True

while active == True:
    age = int(input("What's your age? "))
    if age < 4:
        print("Your ticket is free!")
    elif age == 99: #om loop te breken
        break
    elif 3 < age <12:
        print("Your ticket is 10$.")
    else:
        print("Your ticket is $15.")

# 7.6

print("\n 7.6 \n")

active = True
topping_amount = 0
topping = []

print("You can have 10 toppings on your pizza! Say 'enough' when you're done. ")
while topping_amount < 11:
    temp = input("What'd you like on your pizza?")
    if temp == 'enough':
        print("Bye bye!")
        break
    else:
        topping.append(temp)
        topping_amount = topping_amount + 1
        print("Great! I'll add ", temp, " on your pizza!")

print("I now have a pizza with the following ingredients:")
for x in topping:
    print(x)

# 7.7

print("\n 7.7 \n")

# x = 5
# while x > 3:
#     print("hello")

# 7.8

print("\n 7.8 \n")

sandwich_orders = ['Tosti', 'Hamkaas', 'Gezond', 'Eiersalade', 'Filet American']
finished_sandwiches = []

while sandwich_orders:
    current = sandwich_orders.pop()
    print("Making broodje ", current)
    finished_sandwiches.append(current)
print(finished_sandwiches)

# 7.9

print("\n 7.9 \n")

sandwich_orders = ['Tosti', 'Sate', 'Hamkaas', 'Gezond', 'Eiersalade', 'Sate', 'Filet American', 'Kroket', 'Frikandel', 'Sate', 'Berenklauw', 'Vlamtosti']
finished_sandwiches = []

print('We are you of Sate!')

while 'Sate' in sandwich_orders:
    sandwich_orders.remove('Sate')

while sandwich_orders:
    current = sandwich_orders.pop()
    print("Making broodje ", current)
    finished_sandwiches.append(current)
print(finished_sandwiches)



