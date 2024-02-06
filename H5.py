
#5.1
print("\n 5.1 \n")

auto = "Audi"
leeftijd = 16

print(auto == "audi") #True
print(auto == "volkswagen") #False
print(leeftijd > 15) #True
print(leeftijd < 18) #True
print(leeftijd  == 16) # True
print(auto != "bmw") #True
print(auto == "audi" and leeftijd < 12) #False
print(leeftijd > 18) #False
print(leeftijd < 18 and auto != "audi") #False

#5.2
print("\n 5.2 \n")

#i.o.m. docent overslaan

#5.3
print("\n 5.3 \n")

alien_color = "yellow"
points = 0
while points < 5:
    if alien_color == "green":
        print("You earned 5 points!")
        points = points + 5
    else:
        alien_color = "green"

print("You've got " + str(points) + " points!")

#5.4
print("\n 5.4 \n")

alien_color = "green"
points = 0
if alien_color == "green":
    print("You earned 5 points!")
    points = points + 5
else:
    print("You earned 10 points!")
    points = points + 10

#5.5
print("\n 5.5 \n")

alien_color = "green"
points = 0
while points < 20:
    if alien_color == "green":
        print("You earned 5 points!")
        points = points + 5
        alien_color = "yellow"
    elif alien_color == "yellow":
        print("You earned 10 points!")
        points = points + 10
        alien_color = "red"
    else:
        print("You earned 15 points!")
        points = points + 15


#5.6
print("\n 5.6 \n")

leeftijd = 20

if leeftijd < 2:
    print("Je bent een baby")
elif leeftijd >= 2 and leeftijd < 4:
    print("Je bent een peuter")
elif leeftijd >= 4 and leeftijd < 13:
    print("Je bent een kind")
elif leeftijd >= 13 and leeftijd < 20:
    print("Je bent een tiener")
elif leeftijd >= 20 and leeftijd < 65:
    print("Je bent volwassen")
else:
    print("je bent bejaard")

#5.11
print("\n 5.11 \n")

lijst = list(range(1,10))

for x in lijst:
    if x == 1:
        print(str(x) + "st")
    elif x == 2:
        print(str(x) + "nd")
    elif x == 3:
        print(str(x) + "rd")
    else:
        print(str(x) + "th")

#5.12
print("\n 5.12 \n")

#gedaan

#5.13
print("\n 5.13 \n")

#ok