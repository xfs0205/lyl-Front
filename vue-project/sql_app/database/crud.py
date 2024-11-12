from sqlalchemy import desc
from sqlalchemy.orm import Session
from sql_app.database.schemas import User
from sql_app.database.models import Qixiang,Entropy,User

def get_latest_qixiang_data(db: Session):
    # 查询 Qixiang 表中指定 port 和时间戳最新的记录
    weather = db.query(Qixiang).order_by(desc(Qixiang.time)).first()
    entropy = db.query(Entropy).order_by(desc(Entropy.time)).first()
    return {
        'weather':weather,
        'entropy':entropy
    }


def check_user(db: Session, user: User = None, name: str = None) -> bool:
    if (user is None) and (name is not None):
        existing_user = db.query(User).filter(
            User.name == name,
        ).first()
    elif (user is not None) and (name is None) :
        # 在 User 表中查询是否存在 name 和 password 都匹配的用户
        existing_user = db.query(User).filter(
            User.name == user.name,
            User.password == user.password
        ).first()
    else:
        existing_user = None

    # 如果找到了匹配的用户，返回 True，否则返回 False
    return existing_user is not None
