from main import session
from models.user import User, Role, Address, Preference

admin_role = Role.query.filter_by(slug="admin").first()

user = User(
    first_name="John",
    last_name="Smith",
    email="johnsmith@gmail.com"
)

session.add(user)

user2 = User()
user2.first_name = "Jane"
user2.last_name = "Doe"
user2.email = "janedoe@gmail.com"
session.add(user2)

user3 = User(
    first_name="Jay",
    last_name="Jones",
    email="jayjones@gmail.com"
)

user3.roles.append(admin_role)
user3.addresses.append(
    Address(
        road_name="34 main road",
        postcode="IG114XE",
        city="London",
    )
)
user3.preference = Preference(
    language="English",
    currency="GBP",
)
session.add(user3)

session.commit()
