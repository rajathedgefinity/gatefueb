# ALL Pydantic Models will GO Here.

from pydantic import BaseModel


class Usr(BaseModel):
    email: str
    passwd: str
    is_active: bool = False
    is_admin: bool = False


class Prof(BaseModel):
    f_name: str
    l_name: str
    u_name: str
    mobile: str
    gender: str


class House(BaseModel):
    comm_name: str
    comm_blok: str
    comm_numb: str
