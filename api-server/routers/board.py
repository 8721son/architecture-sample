from fastapi import APIRouter

router = APIRouter(
    prefix='/board'
)

@router.get('/')
def getBoard():
    return {'data':'1'}