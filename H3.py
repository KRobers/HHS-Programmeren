#3.1
print("\n 3.1 \n")

vrienden = ["Henk", "Piet", "Jan", "Gerard", "Johan"]
for x in vrienden:
    print(x)

#3.2
print("\n 3.2 \n")

for x in vrienden:
    print("Hallo "+ x)

#3.3
print("\n 3.3 \n")

fav_food = ["Pizza", "Pasta", "Wafels", "Nasi"]
print("Mijn allerliefste eten is: " + fav_food[1])
print("Daarna komt " + fav_food[0])
print("Dan komt " + fav_food[3])
print("Maar ik houd niet van " + fav_food[2])

print("\n 3.4 \n") #3.4
invite_list = ["Isaac Newton", "Albert Einstein", "Galileo Galilei"]
for x in invite_list:
    print(x + " graag nodig ik u uit voor het eten.")

print("\n 3.5 \n") #3.5
invite_list = ["Isaac Newton", "Albert Einstein", "Galileo Galilei"]
for x in invite_list:
    print(x + " graag nodig ik u uit voor het eten.")

print(invite_list[1] + " kan helaas niet komen")
invite_list.pop(1)
invite_list.append("Nikola Tesla")
for x in invite_list:
    print(x + " graag nodig ik u uit voor het eten.")

#3.6
print("\n 3.6 \n")

print("Ik heb een grotere tafel gevonden")
invite_list.insert(1, "Max Planck")
invite_list.insert(0, "Richard Feynman")
invite_list.append("Niels Bohr")

for x in invite_list:
    print(x + " graag nodig ik u uit voor het eten.")

#3.7
print("\n 3.7 \n")

print("Schijnbaar kan ik toch maar met twee mensen uit eten.")

i = len(invite_list)

while i > 2:
    print(invite_list[0] + " sorry u kan toch niet mee")
    invite_list.pop(0)
    i = len(invite_list)

for x in invite_list:
    print(x + " graag nodig ik u alsnog uit voor het eten.")

del invite_list[0]
del invite_list[0]

print(invite_list)

#3.8
print("\n 3.8 \n")

places = ["New York", "Mexico City", "Machu Picchu", "Kathmandu", "Lima", "Seoul"]
print(places) #origineel

print(sorted(places)) #alfabetisch
print(places) #origineel
print(sorted(places, reverse=True))#ongekeerd alfabetisch
print(places) #origineel
places.reverse()
print(places) # omgekeerd
places.reverse()
print(places) #orginileel
places.sort()
print(places)#alfabetisch
places.sort(reverse=True)
print(places) #mgekeerd alfabetrisch

#3.9
print("\n 3.9 \n")

invite_list = ["Isaac Newton", "Albert Einstein", "Galileo Galilei", "Max Planck", "Richard Feynman", "Niels Bohr"]

i = len(invite_list)
print("Er komen " + str(i) + "mensen op het diner")

#3.10
print("\n 3.10 \n")

#Zie 3.8, praktisch dezelfde opdracht
print("Zie 3.8, praktisch dezelfde opdracht")

#3.11
print("\n 3.11 \n")

#print(invite_list[9])
