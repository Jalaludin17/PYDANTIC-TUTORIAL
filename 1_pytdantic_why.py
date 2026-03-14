def insert_patient_data(name: str, age: int):
    if type(name)==str  and type(age)==int:
        print(name)
        print(age)
        print("inserted into database")
    else:
        raise TypeError("name must be a string and age must be an integer")

insert_patient_data("jalal", 27)

def update_patient_data(name: str, age: int):
    if type(name)==str  and type(age)==int:
        print(name)
        print(age)
        print("data updated in database")
    else:
        raise TypeError("name must be a string and age must be an integer")

update_patient_data("jalal", 27)

 