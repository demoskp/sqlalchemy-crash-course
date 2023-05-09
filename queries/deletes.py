from main import session
from models.user import User

user = User.query.first()

print(user)


session.delete(user)
session.commit()


user = User.query.first()

print(user)