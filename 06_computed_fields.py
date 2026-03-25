from pydantic import BaseModel, EmailStr, AnyUrl, Field, computed_field
from typing import List, Dict, Optional, Annotated

class Patient(BaseModel):  
    name: str
    email: EmailStr  #custom type for email validation
    linked_url: str
    age: int
    weight: float
    height: float
    married: bool
    allergies: List[str] 
    contact_details: Dict[str, str]

    @computed_field
    @property
    def compute_bmi(self) -> float:
        bmi= self.weight / (self.height ** 2)
        return round(bmi, 2)
    
def update_patient_data(patient: Patient):
    print('name : ',patient.name)
    print('email : ',patient.email)
    print('linked_url : ',patient.linked_url)
    print('age : ',patient.age)
    print('weight : ',patient.weight)
    print('height : ',patient.height)
    print('bmi : ',patient.compute_bmi)
    print('married : ',patient.married)
    print('allergies : ',patient.allergies)
    print('contact_details : ',patient.contact_details)
    print("updated into database")

pateint_info = {
    'name': 'jalal',
    'email':'abc@ICB.com',
    'linked_url': 'https://www.example.com',   
    'age': 39,
    'weight': 70.5,
    'height': 1.75,
    'married': True,
    'allergies': ['pollen', 'dust'],
    'contact_details': {'phone': '023-45678900'}
}
patient1 = Patient(**pateint_info)

update_patient_data(patient1)