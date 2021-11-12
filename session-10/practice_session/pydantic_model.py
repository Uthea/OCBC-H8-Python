from pydantic import BaseModel, EmailStr, constr


class AvocadoBodyModel(BaseModel):
    date: str
    avgprice: float
    totalvol: int
    avo_a: int
    avo_b: float
    avo_c: float
    type: int
    regionid: int
