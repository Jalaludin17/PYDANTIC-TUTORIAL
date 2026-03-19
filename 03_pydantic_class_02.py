from pydantic import BaseModel, EmailStr
from typing import List, Dict, Optional

class Patient(BaseModel):
    name: str
    email: EmailStr
    age: int
    weight: float
    married: bool
    allergies: Optional[List[str]] = None  # imported List to use here
    contact_details: Dict[str, str]

#all above fields are required, if any of them is missing, it will raise a validation error. 
# To make them optional, we can use Optional from typing module and set default value to None.
#as used for ellergies

def insert_patient_data(patient: Patient):
    print(patient.name)
    print(patient.age)
    print(patient.weight)
    print(patient.married)
    print(patient.ellergies)
    print(patient.contact_details)
    print("inserted into database")

def update_patient_data(patient: Patient):
    print(patient.name)
    print(patient.age)
    print(patient.weight)
    print(patient.married)
    print(patient.ellergies)
    print(patient.contact_details)
    print("updated into database")

pateint_info = {
    'name': 'jalal',
    'age': 27,
    'weight': 70.5,
    'married': True,
    #'ellergies': ['pollen', 'dust'],
    'contact_details': {'email': 'jalal@example.com', 'phone': '023-45678900'}
}
patient1 = Patient(**pateint_info)

insert_patient_data(patient1)