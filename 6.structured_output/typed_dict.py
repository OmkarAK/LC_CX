from typing import TypedDict

class Person(TypedDict):
    name : str
    age : int

person : Person = {'name':'James','age': 30}

print(person)