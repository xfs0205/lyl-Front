from fastapi import FastAPI, Depends, HTTPException, Response
from sqlalchemy.orm import Session
from fastapi.middleware.cors import CORSMiddleware
from database.database import get_db
from database.crud import get_latest_qixiang_data, check_user
from database.schemas import User
from sql_app.utils import generate_token, get_current_user

app = FastAPI()

# 添加CORS中间件，允许特定来源的请求
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get('/get')
async def get_data(current_user: str = Depends(get_current_user), db: Session = Depends(get_db)):
    if check_user(db=db, name=current_user):
        data = get_latest_qixiang_data(db)
        return data
    else:
        return []


@app.post('/login')
async def login_cookie(user: User, db: Session = Depends(get_db)):
    if check_user(db, user):
        token, expiration_time = generate_token(user.name)
        response = Response(content="success")
        response.set_cookie(
            key="access_token",
            value=token,
            expires=expiration_time,
            httponly=True,
            max_age=60,  # 24小时
            # secure = True,  # 在生产中，确保只在HTTPS上发送Cookie
            # samesite = "lax",
            path="/",
        )
        return response
    else:
        raise HTTPException(status_code=401, detail="Incorrect username or password")


@app.get('/verify')
async def cookie_verify(current_user: str = Depends(get_current_user), db: Session = Depends(get_db)):
    if check_user(db=db, name=current_user):
        return True
    else:
        return False


# 以下代码仅在直接运行此文件时执行
if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="localhost", port=8899)
