# 1st python file hello.py

"""
hello.py
"""

from datetime import datetime

print("hello")

print("world")

a = 10 + 25
tip = 10.0/3.3

print("a: ", a)
print("tip: %.2f %.4f" % (tip, tip))

# string manipulation
simple_thoughts = "It's a beautiful day!"

st_0 = simple_thoughts[0]
st_1 = simple_thoughts[1]

print(st_0, st_1)

fish = "Blue Marlin"

print(len(fish), fish.lower(), fish.upper())
# int to string
print(str(1234))
print("The " + "world " + "is " + "awesome.")

name = "Monette"
print("I am %s" %(name))

# age = raw_input("Please type in your age:")
# print("My age is %s" %(age))

# Datetime library
print(datetime.now())
now = datetime.now()

current_year = now.year
current_month = now.month
current_day  = now.day 
print("%s %s %s" %(current_year,current_month, current_day))
print("%s:%s:%s" %(now.hour,now.minute, now.second))

# Control flow
choice = '1'

if choice == '1':
    print("This is the RPG Room!")
else:
    print("This is a 3D room!")

bool_a = True
bool_b = False

if bool_a:
    print("a is True")
else:
    print("a is False")

################################################
# Tuples
months = ('Jan', 'Feb', 'Mar', 'Apr')
print(months[2])
# Lists
dogs = ['Tad', 'Snoopy', 'Doug', 'Chase', 'Madoka']
print('dogs:',dogs)
dogs[0] = 'Tiddy'
print('dogs:', dogs)
dogs.append('Tiger')
print('dogs: ', dogs)
# Dictionary
phones = {
    'Catherine Becket': 7895675,
    'Anthony Clarke': 123452
}
print(phones['Catherine Becket'])


# end of file