# Samples of simple python arithmetic.

''' A quick note:  In order to print integers and floats,
they have to follow a comma OR be formatted as a number type.
You can't do the following:

>>> print '3 + 5 = ' + simple_int

This attempts to "concatenate" a number and string together
(which you can't do) and results in an exception. To make it work,
you'd have to change "simple_int" to a string type.
>>> print '3 + 5 = ' + str(simple_int)

See PythonFormatOutput.py for formatting examples.'''


print '# Addition and subtraction.'
simple_int = 3 + 5
print '  3 + 5 = ', simple_int
simple_int = simple_int - 5
print '  Answer - 5 = ', simple_int

print '\n# Incrementing variables'
inc_int = 0
print '  Value = ', inc_int
inc_int =+ 1
print '  Value + 1 = ', inc_int
inc_int =+ 2
print '  Value + 2 = ', inc_int

print '\n# Multiplication'
mult = 2 * 5
print '  2 * 5  = ', mult

print '''
# Division:  Usual rules for dividing integers is in play here.
#            The trick is to make at least one of the values a float
#	     to get around this problem.'''
print '  3 / 5 = ', (3 / 5)
print '  float(3) / 5 = ', (float(3) / 5)
# Doesn't matter which is the float value.
print '  3 / float(5) = ', (3 / float(5))
