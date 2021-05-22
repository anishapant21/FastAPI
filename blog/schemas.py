from pydantic import BaseModel

#pydantic
class Blog(BaseModel):
    title: str
    body: str