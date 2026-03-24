from pydantic import BaseModel, EmailStr, AnyUrl, Field, field_validator, model_validator
from typing import List, Dict, Optional, Annotated

class Patient(BaseModel):  
    name: str
    email: EmailStr  #custom type for email validation
    linked_url: str
    age: int
    weight: float
    married: bool
    allergies: List[str] 
    contact_details: Dict[str, str]

    @model_validator(mode='after')
    def validate_emergency_contact(cls, model):
        if model.age > 60 and 'emergency_contact' not in model.contact_details:
            raise ValueError("Emergency contact is required in contact details")
        return model 
    
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
    'email':'abc@ICB.com',
    'linked_url': 'https://www.example.com',   
    'age': 39,
    'weight': 70.5,
    'married': True,
    'allergies': ['pollen', 'dust'],
    'contact_details': {'phone': '023-45678900'}
}
patient1 = Patient(**pateint_info)

update_patient_data(patient1)