#6.1
print("\n 6.1 \n")

kaj = {
    "voornaam" : "Kaj",
    "Achternaam" : "Robers",
    "Straatnaam": "Snoekbaarssingel",
    "Postcode": "2492MH",
    "Huisnummer": 42,
    "Stad": "Den Haag",
}
print(kaj)

#6.3
print("\n 6.3 \n")

woordenboek = {

    "Dictionaries": "Dictionaries are used to store data values in key",
    "List": "Lists are used to store multiple items in a single variable.",
    "For-loop": "A for loop is used for iterating over a sequence.",
    "String": "Strings in python are surrounded by either single quotation marks, or double quotation marks.",
    "Integer": "Int, or integer, is a whole number, positive or negative, without decimals, of unlimited length."
}

for x in woordenboek:
    print(x + ": " + woordenboek[x])


#6.4

print("\n 6.4 \n")

#Al goed gedaan in vorige opdracht. Meer toevoegen veel tikwerk.

#6.5
print("\n 6.5 \n")

rivers = {

    "Nile": "Egypt",
    "Amazon": "Brazil",
    "Yangtze": "China",
    "Mississippi": "United States",
    "Rhine": "Germany"
}

for x in rivers:
    print("The " + x + " runs through " + rivers[x])

for x in rivers:
    print(x)

for x in rivers:
    print(rivers[x])

#6.6

print("\n 6.6 \n")

favorite_languages = {
    'jen': 'python',
    'Daan': '',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    'Henk': '',
    'Piet': '',

 }

for name, language in favorite_languages.items():

    if language != '':
        print(name.title() + ", thank you for taking the poll")
    else:
        print(name.title()+ ", what's your favorite language?")
        favorite_languages.update({name: input()})

for name, language in favorite_languages.items():
    print(name + language)


#6.7

print("\n 6.7 \n")

kaj = {
    "voornaam" : "Kaj",
    "Achternaam" : "Robers",
    "Straatnaam": "Snoekbaarssingel",
    "Postcode": "2492MH",
    "Huisnummer": 42,
    "Stad": "Den Haag",
}

sandra = {
    "voornaam" : "Sandra",
    "Achternaam" : "Robers",
    "Straatnaam": "Snoekbaarssingel",
    "Postcode": "2492MH",
    "Huisnummer": 42,
    "Stad": "Den Haag",
}

john = {
    "voornaam" : "John",
    "Achternaam" : "Robers",
    "Straatnaam": "Snoekbaarssingel",
    "Postcode": "2492MH",
    "Huisnummer": 42,
    "Stad": "Den Haag",
}

mensen = [kaj, john, sandra]

for x in mensen:
    print(x)

#6.11

print("\n 6.11 \n")

cities = {
    'Amsterdam':{
        'Inwoners': 850000,
        'Land':'Nederland',
        'Feit': 'Hoofdstad'
    },
    'Den Haag': {
        'Inwoners': 500000,
        'Land':'Nederland',
        'Feit': "Regering"
    },
    'Rotterdam': {
        'Inwoners': 650000,
        'Land':'Nederland',
        'Feit': 'Erasmusbrug'
    }
}

for x, y in cities.items():
    print(x)
    print(y)

#6.12

print("\n 6.12 \n")

#Veel tikwerk om uit te breiden