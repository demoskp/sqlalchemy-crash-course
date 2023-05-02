from main import session
from models.user import User, Preference

user_preference = (
    Preference.query
    .join(Preference.user)
    .filter(User.email == "johndoe@example.com")
    .first()
)

user_preference.currency = "GBP"
session.commit()

print(user_preference.currency)

User.query \
    .filter(User.first_name == "John") \
    .filter(User.last_name == "Doe") \
    .update({"email": "johndoe@gmail.com"})


print(User.query.first().email)
