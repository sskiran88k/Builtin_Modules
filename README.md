# Builtin_Modules

import os
a=os.getcwd()
print(a)

import random
print(random.random())
print(random.randint(1,100))

import math
print(math.pi)

#Convert from Python to JSON:
import json
data={
    "Python":90,
    "EMWTL":70,
    "DLD":80,
    "CS":90,
    "A.Cir":80,
    "AC":90
}
data1=json.dumps(data)
print(data1)

#Convert from JSON to Python:
import json
data='{"Python":90,"EMWTL":70,"DLD":80,"CS":90,"A.Cir":80,"AC":90}'
data1=json.loads(data)
print(data1)

from datetime import date
print(date.today())

import itertools
print(list(itertools.repeat("S S Kiran", 10)))

import re
a = "The rain in Spain"
x = re.findall("ai", a)
print(x)

import requests
x = requests.get('https://google.com')
print(x.text)
