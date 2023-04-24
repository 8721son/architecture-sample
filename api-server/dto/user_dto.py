from pydantic import BaseModel

class getUserDTO(BaseModel) :
    score : str
    img : str
    username : str
    
class saveUserDTO(BaseModel):
    username : str
    id : str
    password : str