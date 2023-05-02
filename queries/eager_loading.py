from sqlalchemy.orm import joinedload, subqueryload, contains_eager

from models.user import User, Address

users = (
    User.query
    .join(User.addresses)
    .filter(Address.city == "London")
    .options(contains_eager(User.addresses))
    .all()

)

for user in users:
    print(user.addresses)

