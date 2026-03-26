#Now we will use the exported data into json or dict format to create the model instance again
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
    
# 1. Open and read the file
with open("patient.json", "r") as file:
    json_data = file.read()

# 2. Re-create the Patient object using model_validate_json
restored_patient = Patient.model_validate_json(json_data)

# 3. Now you can use it just like the original!
print(f"Restored Patient: {restored_patient.name}")
print(f"Gender: {restored_patient.gender}")
print(f"Age: {restored_patient.age}")
print(f"City: {restored_patient.address.city}")


#for multiple patients
# from pydantic import TypeAdapter
# import json

# # Imagine your file contains: [{"name": "John"...}, {"name": "Jane"...}]
# with open("all_patients.json", "r") as f:
#     raw_data = f.read()

# # Create an adapter for a list of Patients
# adapter = TypeAdapter(list[Patient])
# patients_list = adapter.validate_json(raw_data)

# for p in patients_list:
#     print(p.name)