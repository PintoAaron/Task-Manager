from pydantic import BaseModel, EmailStr


class CustomerIn(BaseModel):
    first_name: str
    last_name: str
    password: str
    phone: str = None
    email: EmailStr


class CustomerOut(BaseModel):
    id: int
    username: str
    email: EmailStr


class UserLogin(BaseModel):
    email: EmailStr
    password: str


class TaskOut(BaseModel):
    title: str
    description: str
    time: str
    status: str


class TaskIn(BaseModel):
    title: str
    description: str
    time: str
