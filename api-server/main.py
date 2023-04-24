from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI
from routers import user,board

# 라우터 쓰는 이유
# api를 효율적으로 관리하기 위해서 (서비스별 파일 분리 )
# 엔드포인트

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    # api서버 도메인
    # 배포시 변경 
    allow_origins = ['http://localhost:3000'],
    # credentials -> true -> origin '*' 사용 못함
    allow_credentials =True,
    # get,post,put
    allow_methods=["*"],
    # header
    allow_headers=["*"]
)

def add_route(app) :
    app.include_router(user.router)
    app.include_router(board.router)


add_route(app)