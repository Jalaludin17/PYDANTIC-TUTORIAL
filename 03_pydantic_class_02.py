from pydantic import BaseModel, EmailStr, AnyUrl, Field
from typing import List, Dict, Optional, Annotated

class Patient(BaseModel):  
    name: Annotated[str, Field(max_length=50, title="Patient Name", description="The name of the patient. It should be a string with a maximum length of 50 characters.", examples=["John Doe", "Ali"])] #max_length is used to set the maximum length of the string, title and description are used for documentation purposes.
    email: EmailStr  #custom type for email validation
    linked_url: Optional[AnyUrl] = None #custom type for url validation, 
    age: int = Field(gt=15, lt=40)
    weight: Annotated[float, Field(gt=0, strict=True)] #gt means greater than 0
    married: Annotated[bool, Field(default=None, description="Marital status of the patient. ")] #description is used for documentation purposes.
    allergies: Annotated[Optional[List[str]], Field(default=None, description="List of allergies the patient has. ")] #description is used for documentation purposes.
    contact_details: Dict[str, str]

#all above fields are required, if any of them is missing, it will raise a validation error. 
# To make them optional, we can use Optional from typing module and set default value to None.
#as used for ellergies

#The Field function is not only used to set defualt values and constraints, 
# but also for adding metadata to the fields, which can be used for documentation purposes 
# or for generating API schemas. it is used with Annotated from typing module.

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