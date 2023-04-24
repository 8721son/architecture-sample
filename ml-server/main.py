from fastapi import FastAPI
import uvicorn
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.tree import plot_tree
import matplotlib.pyplot as plt

from fastapi.middleware.cors import CORSMiddleware

from util import func
from dto import tree_dto
import base64

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    # api서버 도메인
    allow_origins = ['http://localhost:8001'],
    # credentials -> true -> origin '*' 사용 못함
    allow_credentials =True,
    # get,post,put
    allow_methods=["*"],
    # header
    allow_headers=["*"]
)

# 데이터셋 -> 계속 추가된다 -> 경사하강법 돌릴거면 데이터를 매번 로드
# 데이터셋이 추가가 안되거나, 일정 주기로 업데이트 (자주 추가가 안되는) -> 데이터셋 최초에 한번 로드

def tree() :
    data = pd.read_csv('https://bit.ly/wine_csv_data')
    input = data[['alcohol','sugar','pH']].to_numpy()
    target = data['class'].to_numpy()
    train_input,test_input,train_target,test_target = train_test_split(input,target)
    dt = DecisionTreeClassifier()
    dt.fit(train_input,train_target)
    return train_input,train_target,test_input,test_target,dt

train_input,train_target,test_input,test_target,dt = tree()
    
def draw_tree() :
    plot_tree(dt,max_depth=3,feature_names=['alcohol','sugar','pH'],filled=True)
    plt.savefig('./img/tree.png',dpi=400)
    
draw_tree()
    
@app.get("/")
async def root() :
    score = dt.score(test_input,test_target)
    
    # img -> base64 인코딩
    # with ~ as 
    with open('./img/tree.png','rb') as img :
        b64_img = base64.b64encode(img.read())
    
    return func.res_generator(
        status_code=200,
        content=tree_dto.treeDTO(
            score=score,
            img=b64_img
        )
    )
    
    
# requirements.txt (파일명은 바뀌어도 상관없는데, 일반적으로)
# 프로젝트에서 사용중인 라이브러리 목록, 버전 정보
# pip install -r requirements.txt
# requirements.txt 안에 있는 내용을 읽어서 모든 라이브러리를 다 다운받아줌