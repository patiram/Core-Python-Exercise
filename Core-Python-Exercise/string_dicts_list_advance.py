person = {"name":"patiram",  "age":"26"}

sentence = "My name is {} and I am {} years old".format(person['name'], person['age'])

print(sentence)

l = ['patiram', 25]

sentence = "My name is {0[name]} and I am {0[age]} years old.".format(person)

print(sentence)

sentence = "My name is {0[0]} and I am {0[1]} years old.".format(l)

print(sentence)

class Person(object):
	"""docstring for  Person"""
	def __init__(self, name, age):
		super( Person, self).__init__()
		self.name = name
		self.age = age

p1 = Person("patiram", 26)
sentence = "My name is {0.name} and I am {0.age} years old.".format(p1)
print(sentence)


#keyword arguments

person = {"name":"patiram", "age":25}

sentence = "My name is {name} and I am {age} years old.".format(**person)

print(sentence)


for i in range(1,11):
	sentence = "The value is {:02}".format(i) #padding 0 to one digit 00 01 02 ... 10
	print(sentence)

pi = 3.14159265


sentence = 'pi is equal to {:.3f}'.format(pi)
print(sentence)


sentence = '1MB is equal to {:,.2f} bytes'.format(1000**2)
print(sentence)

import datetime
my_date = datetime.datetime(2016, 9, 24, 12, 30, 45)

sentence = '{:%B %d, %Y}'.format(my_date)
print(sentence)

import datetime
my_date = datetime.datetime(2016, 9, 24, 12, 30, 45)


import datetime
my_date = datetime.datetime(2016, 9, 24, 12, 30, 45)

sentence = '{0:%B %d, %Y} fell on a {0:%A} and was the {0:%j} day of the year'.format(my_date)

print(sentence)







		