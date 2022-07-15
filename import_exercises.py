## Import and test 3 of the functions from your function_exercises file.
## Import each function in a different way:

from function_exercises import is_two
##is_two()
from function_exercises import is_vowel
##is_vowel()
from function_exercises import calc_discount
##calc_discount()
##
#### Run an interactive python session and import the function_exercises module.
#### Call the is_vowel function using the '.' syntax.
##
import function_exercises
is_vowel()
##
#### Create a file named import_exericses.py.
#### Within this file, use from to import the calculate_tip function directly.
#### Call this function with values you choose and print the result.
from function_exercises import calculate_tip
calculate_tip()
####total bill = $67.58, tip 20% = $13.52

#### Create a jupyter notebook named import_exercises.ipynb.
#### Use from to import the get_letter_grade function and give it an alias.
#### Test this function in your notebook.

#### Make sure your code that tests the function imports is run from the same
#### directory that your functions exercise file is in.

#### Read about and use the itertools module from the python standard
#### library to help you solve the following problems:

import itertools as it

## How many different ways can you combine the letters from "abc" with the numbers 1, 2, and 3?
print(len(list(it.combinations('abc123',2))))
##15 unique combinations

## How many different combinations are there of 2 letters from "abcd"?
print(len(list(it.combinations('abcd',2))))
## 6 unique combinations

## How many different permutations are there of 2 letters from "abcd"?
print(len(list(it.permutations('abcd',2))))
## 12 permutations

## Save this file as profiles.json inside of your exercises directory (right click -> save file as...).
## Use the load function from the json module to open this file.
import pprint
import json

####try:
####    json.load(open('profiles.json'))
####except json.decoder.JSONDecodeError:

pprint.pprint(json.load(open('profiles.json')))
prof = json.load(open('profiles.json'))

## Your code should produce a list of dictionaries. Using this data, write some code that calculates 
## and outputs the following information:

    ##Total number of users

x = len(prof)
print(x)

#19 users

    ##Number of active users

i = []
for n in prof:
    if n["isActive"] == True:
        i.append(n)
x = len(i)
print(x)
# 9 active users

    ##Number of inactive users

i = []
for n in prof:
    if n["isActive"] != True:
        i.append(n)
x = len(i)
print(x)
# 10 inactive users

    ##Grand total of balances for all users

i = []
for n in prof:
    a = n["balance"].strip().replace("$","").replace(",", "_")
    b = float(a)
    i.append(b)
x = sum(i)
print(x)
# $52,667.02

    ##Average balance per user

i = []
for n in prof:
    a = n["balance"].strip().replace("$","").replace(",", "_")
    b = float(a)
    i.append(b)
x = round((sum(i)/len(i)), 2)
print(x)
# $2771.95
    
    ##User with the lowest balance

i = []
for n in prof:
    a = n["balance"].strip().replace("$","").replace(",", "_")
    b = float(a)
    i.append(b)
x = min(i)
print(x)
y = " ".join([f["name"] for f in prof if float(f["balance"].strip().replace("$","").replace(",", "_")) == x])
print(y)
# Avery Flynn

    ##User with the highest balance

i = []
for n in prof:
    a = n["balance"].strip().replace("$","").replace(",", "_")
    b = float(a)
    i.append(b)
x = max(i)
print(x)
y = " ".join([f["name"] for f in prof if float(f["balance"].strip().replace("$","").replace(",", "_")) == x])
print(y)
# Fay Hammond

    ##Most common favorite fruit

i = []
for n in prof:
    a = n["favoriteFruit"]
    i.append(a)
for p in i:
    x = i.count(p)
    print(x, [p])
# Most common favorite fruit is strawberry with 9 enthusiasts.

    ##Least common favorite fruit

# Least common favorite fruit is apple with 4 enthusiasts.

    ##Total number of unread messages for all users

i = []
for n in prof:
    z = ""
    for y in n["greeting"]: 
        if y.isdigit() == True:
            z = z.strip() + y.strip()    
    w = int(z)
    i.append(w)
x = sum(i)
print(x)

