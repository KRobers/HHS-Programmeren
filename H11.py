import unittest


def city_functions(city, country, population=None):

    if population:
        city_country_population = city.title() + ', ' + country.title() + ', ' + str(population)
        return city_country_population
    else:
        city_country = city.title() + ', ' + country.title()
        return city_country


class test_citycase(unittest.TestCase):

    def test_city_country(self):
        city_country = city_functions('santiago', 'chile')
        self.assertEqual(city_country, 'Santiago, Chile')
    def test_city_country_population(self):
        city_country_pop = city_functions('paris', 'france', 1600000)
        self.assertEqual(city_country_pop, 'Paris, France, 1600000')

if __name__ == '__main__':
    unittest.main()

#11.3

class employee():

    def __init__(self, fname, lname, salary):
        self.first_name = fname
        self.last_name = lname
        self.annual_salary = salary

    def give_raise(self, amount=5000):
        self.annual_salary = self.annual_salary + amount

class TestEmployee(unittest.TestCase):
    def setUp(self):
        self.myemployee = employee('Kaj', 'Robers', 1000)

    def test_give_default_raise(self):
        self.myemployee.give_raise()
        self.assertEqual(self.myemployee.annual_salary, 6000)

    def test_give_custom_raise(self):
        self.myemployee.give_raise(10000)
        self.assertEqual(self.myemployee.annual_salary, 11000)

if __name__ == '__main__':
    unittest.main()