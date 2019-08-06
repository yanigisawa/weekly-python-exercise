# The "operator" module is a fantastic part of the Python standard library, providing functions that implement all of Python's operators. One of the most useful functions in there, I've found, is "itemgetter".  It basically works like square brackets.  You invoke itemgetter with one or more arguments, and what you get back is a function that retrieves one or more elements from its own arguments.

# Let me try to make it a bit clearer with two examples:
#     >>> import operator

#     >>> mylist = [[10, 20, 30], [40, 50, 60], [70, 80, 90]]

#     >>> final = operator.itemgetter(-1)
#     >>> [final(sublist)
#     ...  for sublist in mylist]
#     [30, 60, 90]

# In other words, operator.itemgetter(-1) returned a function that, when applied to a list (or tuple, or string) returns the final element of that sequence.

# We can also invoke operator.itemgetter with more than one argument.  For example:
#     >>> first_and_last = operator.itemgetter(0,-1)

#     >>> [first_and_last(sublist)
#     ...  for sublist in mylist]
#     [(10, 30), (40, 60), (70, 90)]

# The function returned by operator.itemgetter(0,-1) returns a two-element tuple.

# This week's exercise is to implement your own version of operator.itemgetter.  If invoked with one argument, it should return a function that returns a single element of its argument.  If invoked with multiple arguments, it should return a function that returns a tuple.

# Note that the function returned by itemgetter might be invoked on a string, list, tuple, or even a dictionary -- or anything else that can be indexed with square brackets.

# So it should be possible to do this:
#     g1 = mygetter(-1)
#     g1([10, 20, 30])  # returns 30

#     g2 = mygetter(0, -1)
#     g2([10, 20, 30])  # returns (10, 30)

#     g3 = mygetter('b')
#     d = {'a':1, 'b':2, 'c':3}
#     g3(d)             # returns 2

# I'll be back on Monday with my solution.

# Reuven

from solution import mygetter

def test_one_pos_index():
    s = 'abcde'
    i2 = mygetter(2)

    assert i2(s) == 'c'

def test_one_neg_index():
    s = 'abcde'
    i2 = mygetter(-2)

    assert i2(s) == 'd'

def test_one_key():
    d = {'a':1, 'b':2, 'c':3}
    ka = mygetter('a')

    assert ka(d) == 1

def test_multiple_indexes():
    s = 'abcde'
    i21 = mygetter(2,1)

    assert i21(s) == ('c', 'b')

def test_multiple_keys():
    d = {'a':1, 'b':2, 'c':3}
    kab = mygetter('a', 'b')

    assert kab(d) == (1, 2)