#4.1
print("\n 4.1 \n")

pizza = ["pepperoni", "margaritha", "caprese"]
for x in pizza:
    print(x)

for x in pizza:
    print("Ik houd van " + x + " pizza")

print("Ik houd echt zoveel van pizza!")

#4.2
print("\n 4.2 \n")

dieren = ["hond", "kat", "cavia"]
for x in dieren:
    print(x)

for x in dieren:
    print("Een " + x + " maakt een leuk huisdier")

print("Dit zijn allemaal leuke huisdieren!")

#4.3
print("\n 4.3 \n")

twenty = []
i = 1

while i < 21:
    twenty.append(i)
    i = i + 1

print(twenty)

#4.4
print("\n 4.4 \n")

million = []
i = 1

while i < 101: #100 gedaan ivm performance
    million.append(i)
    i = i + 1

print(million)

#4.5
print("\n 4.5 \n")

print(min(million))
print(max(million))
print(sum(million))

#4.6
print("\n 4.6 \n")

odd_numbers = list(range(1,20,2))
for x in odd_numbers:
    print(x)

#4.7
print("\n 4.7 \n")

threes = list(range(3,31 , 3))
for x in threes:
    print(x)

#4.8
print("\n 4.8 \n")

kwadraat = range(1,11)
for x in kwadraat:
    som = x**2
    print(som)

#4.9
print("\n 4.9 \n")

#eerste 10 machten van 2
kwadraat = []
getal = 2
macht = 1

while macht < 11:
    kwadraat.append(getal**macht)
    macht = macht + 1

print(kwadraat)

#4.10
print("\n 4.10 \n")

pizza = ["pepperoni", "margaritha", "caprese", "tonno",
         "carpaccio", "funghi","hawaii", "bbq chicken",
         "pesto", "vier kazen"]
print(pizza[:3])
print(pizza[3:6])
print(pizza[7:])

#4.11
print("\n 4.11 \n")

pizza.append("shoarma")
vriend_pizza = ["pepperoni", "margaritha", "caprese", "tonno",
                "carpaccio", "funghi","hawaii", "bbq chicken",
                "pesto", "vier kazen"]
vriend_pizza.append("doner")

print("Mijn favoriete pizza's zijn:")
for x in pizza:
    print(x)

print("\n")

print("Zijn favoriete pizza's zijn:")
for x in vriend_pizza:
    print(x)

#4.12
print("\n 4.12 \n")

#zie hierboven in mijn voorbeelden
