# # build-in data types
#
# age = 24
# print(id(age))
# print(type(age))
# age = 24 + 1
# print(id(age))
# class Person:
#     def __init__(self, age):
#         self.age = age
#
#
# person = Person(age=24)
# print(id(person))
# person.age = 25;
#
# print(id(person))


# Numbers
a = 3
b = 5
a+b  # addition
b-a  # subtraction
print(a//b)  # integer division
print(a/b)   # true division
a * b  # multiplication 15
b ** a  # power operator
2 ** 1024  # a very big number, Python handles it gracefully

int(1.75)
10 % 4  # remainder of the division 10 // 4

#  Booleans

int(True)  # True behaves like 1
int(False)  # False behaves like 0
bool(1)  # 1 evaluates to True in a boolean context
bool(-42)  # and so does every non-zero number True
bool(0)  # 0 evaluates to False
not True  # False
True and True  # True
False or True  # True
1 + True  # 2
False + 42

# float
pi = 3.1415926536  # how many digits of PI?
radius = 7.5
area = pi * (radius ** 2)

print(3 * 0.1 - 0.3)  # hmmm something interesting here

#  complex number
c = 3.14 + 2.73j
c.real  # real part 3.14
c.imag  # imaginary part 2.73
c.conjugate()  # conjugate of A + Bj is A - Bj (3.14-2.73j)

# fractions and decimal

from fractions import Fraction
Fraction(10, 6)  # mad hatter?
Fraction(5, 3)  # notice it's been reduced to lowest terms
Fraction(1, 3) + Fraction(2, 3)  # 1/3 + 2/3 = 3/3 = 1/1 Fraction(1, 1)
f = Fraction(10, 6)  # what happens here
f.numerator  # 5
f.denominator  # u tell me

# Decimal

from decimal import Decimal as D  # rename for brevity
D(3.14)  # pi, from float, so approximation issues Decimal('3.140000000000000124344978758017532527446746826171875')
D('3.14')  # pi, from a string, so no approximation issues Decimal('3.14')
D(0.1) * D(3) - D(0.3)  # from float, we still have the issue Decimal('2.775557561565156540423631668E-17')
D('0.1') * D(3) - D('0.3')  # from string, all perfect Decimal('0.0')

# immutable sequences  strings, tuples, and bytes.

# 4 ways to make a string
str1 = 'This is a string. We built it with single quotes.'
str2 = "This is also a string, but built with double quotes."
str3 = '''This is built using triple quotes, 
 so it can span multiple lines.'''
str4 = """This too 
 is a multiline one 
  built with triple double-quotes."""
len(str1)

# encoding and decoding

s = "This is üŋícode"  # unicode string: code points
type(s)  # <class 'str'>
encoded_s = s.encode('utf-8')  # utf-8 encoded version of s
print(encoded_s)  # b'This is \xc3\xbc\xc5\x8b\xc3\xadc0de'   result: bytes object
type(encoded_s)  # another way to verify it <class 'bytes'>
encoded_s.decode('utf-8')  # let's revert to the original 'This is üŋíc0de'
bytes_obj = b"A bytes object"  # a bytes object >>> type(bytes_obj) <class 'bytes'>

#  indexing string
s = "The trouble is you think you have time."
s[0]  # indexing at position 0, which is the first char 'T'
s[5]  # indexing at position 5, which is the sixth char 'r'
s[:4]  # slicing, we specify only the stop position 'The '
s[4:]  # slicing, we specify only the start position 'trouble is you think you have time.'
s[2:14]  # slicing, both start and stop positions 'e trouble is'
s[2:14:3]  # slicing, start, stop and step (every 3 chars) 'erb '
s[:]  # quick way of making a copy 'The trouble is you think you have time.'

#  Tuples
t = ()  # empty tuple
type(t) #<class 'tuple'>
one_element_tuple = (42, )  # you need the comma!
three_elements_tuple = (1, 3, 5)
a, b, c = 1, 2, 3  # tuple for multiple assignment
3 in three_elements_tuple  # membership test
a, b = b, a  # this is the Pythonic way to do it

#  Mutable sequence Lists

li = []  # empty list []
list()  # same as [] []
li = [1, 2, 3]  # as with tuples, items are comma separated
num1 = [x + 5 for x in [2, 3, 4]]  # Python is magic [7, 8, 9]
num2 = list((1, 3, 5, 7, 9))  # list from a tuple [1, 3, 5, 7, 9]
greet = list('hello')  # list from a string

#  some methods used with list
a = [1, 2, 1, 3]
a.append(13)  # we can append anything at the end a [1, 2, 1, 3, 13]
a.count(1)  # how many `1` are there in the list? 2
a.extend([5, 7])  # extend the list by another (or sequence) a [1, 2, 1, 3, 13, 5, 7]
a.index(13)  # position of `13` in the list (0-based indexing) 4
a.insert(0, 17)  # insert `17` at position 0 a [17, 1, 2, 1, 3, 13, 5, 7]
a.pop()  # pop (remove and return) last element 7
a.pop(3)  # pop element at position 3 1 a [17, 1, 2, 3, 13, 5]
a.remove(17)  # remove `17` from the list a [1, 2, 3, 13, 5]
a.reverse()  # reverse the order of the elements in the list >>> a [5, 13, 3, 2, 1] >>>
a.sort()  # sort the list >>> a [1, 2, 3, 5, 13]
a.clear()  # remove all elements from the list

#  Now, let's see what are the most common operations you can do with lists:
a = [1, 3, 5, 7]
min(a)  # minimum value in the list 1
max(a)  # maximum value in the list 7
sum(a)  # sum of all values in the list 16
len(a)  # number of elements in the list 4
b = [6, 7, 8]
a + b  # `+` with list means concatenation [1, 3, 5, 7, 6, 7, 8]
a * 2  # `*` has also a special meaning [1, 3, 5, 7, 1, 3, 5, 7

#  more on sorting
from operator import itemgetter
a = [(5, 3), (1, 3), (1, 2), (2, -1), (4, 9)]
sorted(a) # [(1, 2), (1, 3), (2, -1), (4, 9), (5, 3)]
sorted(a, key=itemgetter(0))  # [(1, 3), (1, 2), (2, -1), (4, 9), (5, 3)]
sorted(a, key=itemgetter(0, 1)) # [(1, 2), (1, 3), (2, -1), (4, 9), (5, 3)]
sorted(a, key=itemgetter(1)) # [(2, -1), (1, 2), (5, 3), (1, 3), (4, 9)]
sorted(a, key=itemgetter(1), reverse=True)  # [(4, 9), (5, 3), (1, 3), (1, 2), (2, -1)]

#  sets
small_primes = set()  # empty set
small_primes.add(2)  # adding one element at a time
small_primes.add(3)
small_primes.add(5) #{2, 3, 5}

small_primes.add(1)  # Look what I've done, 1 is not a prime!
small_primes.remove(1)  # so let's remove it
3 in small_primes  # membership test True
4 in small_primes # False
4 not in small_primes  # negated membership test True
small_primes.add(3)  # trying to add 3 again, {2, 3, 5}
#  no change, duplication is not allowed
bigger_primes = set([5, 7, 11, 13])  # faster creation
small_primes | bigger_primes  # union operator `|` {2, 3, 5, 7, 11, 13}
small_primes & bigger_primes  # intersection operator `&` {5}
small_primes - bigger_primes  # difference operator `-` {2, 3}

small_primes = frozenset([2, 3, 5, 7])
bigger_primes = frozenset([5, 7, 11])
small_primes.add(11)  # we cannot add to a frozenset

#  Dictionary
a = dict(A=1, Z=-1)
b = {'A': 1, 'Z': -1}
c = dict(zip(['A', 'Z'], [1, -1]))
d = dict([('A', 1), ('Z', -1)])
e = dict({'Z': -1, 'A': 1})
a == b == c == d == e  # are they all the same?

d = {}
d['a'] = 1  # let's set a couple of (key, value) pairs
d['b'] = 2
len(d)  # how many pairs? 2
d['a']  # what is the value of 'a'? 1
del d['a']  # let's remove `a` d {'b': 2}
d['c'] = 3  # let's add 'c': 3
'c' in d  # membership is checked against the keys True
3 in d  # not the values

'e' in d # False
d.clear()


d = dict(zip('hello', range(5))) #d {'e': 1, 'h': 0, 'o': 4, 'l': 3}
d.keys() # dict_keys(['e', 'h', 'o', 'l'])
d.values()  # dict_values([1, 0, 4, 3])
d.items()  # dict_items([('e', 1), ('h', 0), ('o', 4), ('l', 3)])
3 in d.values() # True
('o', 4) in d.items()

d.popitem()  # removes a random item ('e', 1) >>> d {'h': 0, 'o': 4, 'l': 3}
d.pop('l')  # remove item with key `l` 3
d.pop('not-a-key')  # remove a key not in dictionary:
d.pop('not-a-key', 'default-value')  # with a default value? 'default-value'  # we get the default value
d.update({'another': 'value'})  # we can update dict this way
d.update(a=13)  # or this way (like a function call) >>> d {'a': 13, 'another': 'value', 'h': 0, 'o': 4}
d.get('a')  # same as d['a'] but if key is missing no KeyError 13
d.get('a', 177)  # default value used if key is missing 13
d.get('b', 177)  # like in this case 177
d.get('b')  # key is not there, so None is returned

d.setdefault('a', 1)  # 'a' is missing, we get default value 1 >>> d {'a': 1}
#  also, the key/value pair ('a', 1) has now been added
d.setdefault('a', 5)  # let's try to override the value 1 d {'a': 1}
#  didn't work, as expected

# COLLECTION MODEL
from collections import namedtuple
Vision = namedtuple('Vision', ['left', 'right'])
vision = Vision(9.5, 8.8)
vision[0] # 9.5
vision.left  # same as vision[0], but explicit 9.5
vision.right  # same as vision[1], but explicit

from collections import defaultdict
dd = defaultdict(int)  # int is the default type (0 the value)
dd['age'] += 1  # short for dd['age'] = dd['age'] + 1
dd['age'] = 39
dd['age'] += 1

from collections import ChainMap
default_connection = {'host': 'localhost', 'port': 4567}
connection = {'port': 5678}
conn = ChainMap(connection, default_connection) # map creation
print(conn['port'])  # port is found in the first dictionary 5678
print(conn['host'])  # host is fetched from the second dictionary 'localhost'
print(conn.maps)  # we can see the mapping objects [{'port': 5678}, {'host': 'localhost', 'port': 4567}]
conn['host'] = 'packtpub.com'  # let's add host
print(conn.maps)  # [{'host': 'packtpub.com', 'port': 5678}, {'host': 'localhost', 'port': 4567}]
del conn['port']  # let's remove the port information
print(conn.maps)
print(dict(conn))