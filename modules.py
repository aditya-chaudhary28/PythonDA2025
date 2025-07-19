from functions import greet
from functions import subm

greet()
print(subm(10,5))

# Modules Math
import math

x=10.6
print(math.sqrt(x))
print(math.ceil(x))
print(math.floor(x))
print(math.trunc(x))

print('-'*50)
x=3
print(math.exp(x))
print(math.log10(x))
print()
print(math.sin(90))
print('-'*61)

# Import Random
import random

print(random.random())
print(random.randint(1,10))
print(random.sample([1,2,3,4,5],2))
print(random.choice([1,2,4,7,6]))

import datetime
date_1=datetime.datetime.now()
date_2=datetime.datetime(2023,10,28,2,34)

# =datetime.datetime.now().strftime("%d:%m:%y %H:%M:%S")

print(date_1-date_2)

# collections
from collections import Counter,defaultdict,OrderedDict
lst=[1,2,3,4,5,6,2,4,6,7,8,1,8,9,1,3,5,4,6,]
print(Counter(lst))

# Default Dict

d=defaultdict(int)
d['a'] +=2
print(d)

print('*'*50)
d=OrderedDict()
d['one']=1
d['two']=2
d['three']=3
print(d)