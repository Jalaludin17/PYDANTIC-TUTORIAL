from pydantic import BaseModel, EmailStr, AnyUrl, Field, field_validator
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

    @field_validator('email', mode='after') #mode is for the input value before coersion or after 
    @classmethod
    def email_validator(cls, value):
        #abc@gmail.com must be abc@NBP.com or abc@ICB.com
        valid_domains = ['nbp.com', 'icb.com']
        domain = value.split('@')[-1]
        if domain not in valid_domains:
            raise ValueError(f"Email domain must be one of the following: {', '.join(valid_domains)}")

        return value

    @field_validator('name', mode='after')
    @classmethod
    def transform_name(cls, value):
        return value.upper()  # Convert the name to title case

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