
""" test n°1 - import """
---------------------
>>> print_square = __import__('4-print_square').print_square



""" test n°2 """
	size -> string.
---------------------
>>> print_square('size')
Traceback (most recent call last):
TypeError: size must be an integer



""" test n°3 """
	size -> True.
---------------------
>>> print_square(True)
#


""" test n°4 """
	size -> negative integer.
---------------------
>>> print_square(-4)
Traceback (most recent call last):
ValueError: size must be >= 0



""" test n°5 """
	size -> negative float.
---------------------
>>> print_square(-5.5)
Traceback (most recent call last):
TypeError: size must be an integer



""" test n°6 """
	size -> integer.
---------------------
>>> print_square(0)



""" test n°7 """
	size -> integer.
---------------------
>>> print_square(3)
###
###
###



""" test n°8 """
	size -> integer.
---------------------
>>> print_square(1)
#
