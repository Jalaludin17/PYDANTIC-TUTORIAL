from pydantic import BaseModel 

class Patient(BaseModel):
    name: str
    age: int
    
def insert_patient_data(patient: Patient):
    print(patient.name)
    print(patient.age)
    print("inserted into database")

def update_patient_data(patient: Patient):
    print(patient.name)
    print(patient.age)
    print("updated into database")

#if age is added as a string, it will be converted to int by pydantic(only if it is a number with quotes.)
patient_info = {'name': 'jalal', 'age': '27'}
patient1= Patient(**patient_info)

update_patient_data(patient1)



