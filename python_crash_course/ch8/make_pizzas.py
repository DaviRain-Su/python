# use the module pizza.py
# So we can use the function make_pizza() from pizza.py
# #1
# import pizza # import the module pizza.py
# #2
# from pizza import make_pizza # import the function make_pizza() from pizza.py
# #3
# from pizza import make_pizza as mp # import the function make_pizza() from pizza.py and give it an alias mp
# #4
from pizza import * # import all functions from pizza.py


make_pizza(16, 'pepperoni')
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')
