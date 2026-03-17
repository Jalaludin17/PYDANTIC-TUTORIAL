from pydantic import BaseModel
from typing import List, Dict

class Patient(BaseModel):
    name: str
    age: int
    weight: float
    married: bool
    ellergies: List[str] #imported List to use here
    contact_details: Dict[str, str]

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
    'ellergies': ['pollen', 'dust'],
    'contact_details': {'email': 'jalal@example.com', 'phone': '023-45678900'}
}
patient1 = Patient(**pateint_info)

insert_patient_data(patient1)