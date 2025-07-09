from pydantic import BaseModel, EmailStr, Field
from typing import Optional

class Person(BaseModel):
    name: str = 'Jim'
    age: Optional[int] = None
    email: Optional[EmailStr] = None
    cgpa: float = Field(gt=0, lt=10, default=None, description='Decimal value')

new_person = {'name':'James','age':21,'cgpa':1.1}
new_person2 = {'email':'abc@gmail.com','cgpa':9.1}
new_person3 = {'name':'Jacks','age':20} #Implicit type conversion or coerce

person = Person(**new_person)
person2 = Person(**new_person2)
person3 = Person(**new_person3)
print(person)
print(person.name)

print(person2)
print(person3)

person_json = person.model_dump_json()
print(person_json)