from sqlalchemy import Integer, Column, String
from config import Base

class Test(Base):

    __tablename__ = 'api'

    id =Column(Integer, primary_key=True)
    primKey=Column(String(100), unique=True)
    field1  =Column(String(100))
    field2 =Column(String(100))
    field3=Column(String(100))
    field4  =Column(String(100))
    field5  =Column(String(100))
    iud= Column(String(100))
