from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse

from dto import response

def res_generator(
    status_code:int = 200, error: dict | None =None, content: object | None=None
):
    # 에러일 경우 => code,message 직접 넣어줘야됨
    # 에러가 아닐땐 => code=200, message=""
    encoded_obj = jsonable_encoder(response.ResponseDTO(
        code = error['code'] if error!=None else 0,
        message = error['message'] if error != None else "",
        content = content
    ))
    
    return JSONResponse(status_code=status_code, content=encoded_obj)