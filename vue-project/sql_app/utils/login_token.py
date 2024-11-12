import jwt
from datetime import datetime, timezone, timedelta
from fastapi import Request, HTTPException
from starlette.status import HTTP_401_UNAUTHORIZED

# 加载密钥
SECRET_KEY = "jdlajdjakfbdbfyudfhap"


def generate_token(username: str):
    # 设置token的过期时间为24小时
    expiration_time = datetime.now(timezone.utc) + timedelta(minutes=1)  # 使用 timedelta

    # 创建payload，包含用户信息和过期时间
    payload = {
        'username': username,
        'exp': expiration_time
    }

    # 使用HS256算法和SECRET_KEY签名token
    token = jwt.encode(payload, SECRET_KEY, algorithm='HS256')

    return token, expiration_time


def verify_token(token: str):
    try:
        # 尝试解码token
        payload = jwt.decode(token, SECRET_KEY, algorithms=['HS256'])
        # 如果解码成功，返回True
        return [True, payload]
    except jwt.ExpiredSignatureError:
        # 令牌过期
        print("Token has expired")
    except jwt.InvalidTokenError:
        # 令牌无效
        print("Invalid token")
    except Exception as e:
        # 其他错误
        print(f"An error occurred: {e}")

    # 如果解码失败，返回False
    return [False]


def get_current_user(request: Request):
    token = request.cookies.get("access_token")
    if not token:
        raise HTTPException(
            status_code=HTTP_401_UNAUTHORIZED,
            detail="Access token not found",
            headers={"WWW-Authenticate": "Bearer"},
        )
    result = verify_token(token)
    if not result[0]:
        raise HTTPException(
            status_code=HTTP_401_UNAUTHORIZED,
            detail="Invalid authentication credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )
    return result[1]['username']
