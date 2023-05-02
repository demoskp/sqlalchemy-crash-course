from main import session
from models.user import User, Preference

user = User(first_name="John", last_name="Smith", email="jsmith@gmail.com")

session.add(user)

preference = Preference(language="English", currency="GBP")

something = user.first_name == "John"

if something:
    raise Exception("Something went wrong")

preference.user = user
session.commit()
