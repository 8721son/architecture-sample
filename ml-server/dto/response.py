from pydantic import BaseModel

class ResponseDTO(BaseModel) :
    code : int
    message : str = ""
    content : object | None = None