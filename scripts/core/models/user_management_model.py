from pydantic import BaseModel


class Signup(BaseModel):
    first_name: str
    last_name: str
    email_id: str
    phone_no: str
    password: str
