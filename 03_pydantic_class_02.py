from pydantic import BaseModel, EmailStr, AnyUrl, Field
from typing import List, Dict, Optional

class Patient(BaseModel):  
    name: str = Field(max_length=50)
    email: EmailStr  #custom type for email validation
    linked_url: Optional[AnyUrl] = None #custom type for url validation, 
    age: int = Field(gt=15, lt=40)
    weight: float = Field(gt=0) #gt means greater than 0
    married: bool
    allergies: Optional[List[str]] = None  # imported List to use here
    contact_details: Dict[str, str]

#all above fields are required, if any of them is missing, it will raise a validation error. 
# To make them optional, we can use Optional from typing module and set default value to None.
#as used for ellergies

def insert_patient_data(patient: Patient):
    print(patient.name)
    print(patient.email)
    print(patient.linked_url)
    print(patient.age)
    print(patient.weight)
    print(patient.married)
    print(patient.allergies)
    print(patient.contact_details)
    print("inserted into database")

def update_patient_data(patient: Patient):
    print(patient.name)
    print(patient.email)
    print(patient.linked_url)
    print(patient.age)
    print(patient.weight)
    print(patient.married)
    print(patient.allergies)
    print(patient.contact_details)
    print("updated into database")

pateint_info = {
    'name': 'jalal',
    'email':'abc@example.com',
    'linked_url': 'https://www.example.com',   
    'age': 39,
    'weight': 70.5,
    'married': True,
    #'allergies': ['pollen', 'dust'],
    'contact_details': {'phone': '023-45678900'}
}
patient1 = Patient(**pateint_info)

insert_patient_data(patient1)