#8.1

print("\n 8.1 \n")

def display_message():
    print("We're learing about fucntions!")

display_message()

#8.2

print("\n 8.2 \n")

def favorite_book(title):
    print('My favorite book is', title)

favorite_book("Around the world in 80 days")

#8.3

print("\n 8.3 \n")

def make_shirt(size, text):
    print('I will make a t-shirt in size ', size, ' with the text: ', text)

make_shirt('L', 'Hoi Hoi')
make_shirt(text='Doei doei', size='M')

#8.4

print("\n 8.4 \n")

def make_shirt(size = "Large", text = "I love Python"):
    print('I will make a t-shirt in size ', size, ' with the text: ', text)

make_shirt() #default both
make_shirt(size="Medium") #default message different size
make_shirt(text='I love Java') #default size differnt text
make_shirt('small', 'I love C++'    ) #both different

#8.5

print("\n 8.5 \n")

def describe_city(city, country='Germany'):
    print(city.title(), 'is in ', country)

describe_city('hamburg')
describe_city('berlin')
describe_city('amsterdam')

#8.6

print("\n 8.6 \n")
def city_country(city, country):
    x = city.title() + ', ' + country.title()
    return x

print(city_country('santiago', 'chile'))
print(city_country('amsterdam', 'holland'))
print(city_country('berlin', 'germany'))

#8.7

print("\n 8.7 \n")

def make_album(artist_name, album_title, num_tracks=None):
    album_info = {'artist': artist_name, 'title': album_title}
    if num_tracks:
        album_info['tracks'] = num_tracks
    return album_info

print(make_album('Life of Pablo', 'Kanye'))

#8.8

print("\n 8.8 \n")

active = True

while active:
    input_album = input('Insert album name: ')
    if input_album == 'quit':
        break
    input_artist = input('Insert artist name: ')
    if input_artist == 'quit':
        break

    print(make_album(input_artist, input_album))

#8.9

print("\n 8.9 \n")

magicians = ['David Blaine', 'David Copperfield', 'Hans Kazan', 'Hans Klok', 'Harry Houdini']

def show_magicians(list):
    for x in list:
        print(x)


show_magicians(magicians)

#8.10

print("\n 8.10 \n")

magicians = ['David Blaine', 'David Copperfield', 'Hans Kazan', 'Hans Klok', 'Harry Houdini']

def show_magicians(list):
    for x in list:
        print(x)

def make_great(lijst):
    for i in range(len(lijst)):
        lijst[i] = 'the Great ' + lijst[i]


make_great(magicians)
print(show_magicians(magicians))

#8.11

print("\n 8.11 \n")

magicians = ['David Blaine', 'David Copperfield', 'Hans Kazan', 'Hans Klok', 'Harry Houdini']

def show_magicians(list):
    for x in list:
        print(x)

def make_great(lijst):
    great_magician = []
    for i in lijst:
        magician = 'The great ' + i
        great_magician.append(magician)
    return great_magician

show_magicians(magicians)

great_magician = make_great(magicians)
show_magicians(great_magician)


#8.15 / 16 / 18

print("\n 8.15 / 16 / 18 \n")

# erg makkelijk. veel werk om losse bestanden te gaan maken.