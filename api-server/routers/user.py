from fastapi import APIRouter
import requests
import json
from dto import user_dto
from util import func

router = APIRouter(
    prefix='/user'
)

def getTree():
    res = requests.get('http://127.0.0.1:8000')
    return res

# 머신러닝서버에서 데이터 받아오고,
# db 에서 데이터 가져와서 
# dto 만들어서 리턴하는 기능
@router.get('/')
def getUser():
    res = getTree()
    json_res = json.loads(res.content)
    score = json_res['content']['score']
    img = json_res['content']['img']
    
    # 데이터베이스에서 가져왔다고 가정
    username = '홍길동'
    
    return func.res_generator(
        status_code=200,
        content = user_dto.getUserDTO(
            score=score,
            img=img,
            username=username
        )
    )