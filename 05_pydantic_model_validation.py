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

   