from pydantic import BaseModel

class Address(BaseModel):
    street: str
    city: str
    state: str
    zip_code: str

class Patient(BaseModel):
    name: str
    gender: str
    age: int
    address: Address  # Forward reference to Address model

def update_patient_data(patient: Patient):
    print('name: ', patient.name)
    print('gender: ', patient.gender)
    print('age: ', patient.age)
    print('state: ', patient.address.state)
    print('city: ', patient.address.city)
    print('street: ', patient.address.street)
    print('zip_code: ', patient.address.zip_code)
    print("updated into database")

address_info = {
    'street': '123 Main St',
    'city': 'Anytown',
    'state': 'CA',
    'zip_code': '12345'
}

address1 = Address(**address_info)

patient_info = {
    'name': 'John Doe',
    'gender': 'Male',
    'age': 30,
    'address': address1  # Nested model data
}


patient1 = Patient(**patient_info)



#we can export this model as json or dict 
# and also we can import the data from json or dict to create the model instance

#model_dump will export your model as dictionary
patient_dict = patient1.model_dump()
print(patient_dict)
print(type(patient_dict))

#model_dump_json exports your model as json
patient_json = patient1.model_dump_json()
print(patient_json)
print(type(patient_json))