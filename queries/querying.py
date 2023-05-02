from sqlalchemy import desc

from models.user import User, Role


all_users = User.query.all()
first_user = User.query.first()

# Filter records

# Users called John
johns = User.query.filter_by(first_name="John").all()

# users using gmail
gmail_users = User.query.filter(
    User.email.like("%@gmail.com")
).all()

# Super Administrators
users = (
    User.query
    .join(User.roles)
    .filter(Role.slug == "super-admin")
    .all()
)

# Ordering users by a column
users_by_name = (
    User.query
    .order_by(User.first_name)
    .all()
)

users_by_name_descending = (
    User.query
    .order_by(desc(User.first_name))
    .order_by(desc(User.last_name))
    .all()
)


# Limiting results
first_three_users = User.query.limit(3).all()

# Offsetting results
skip_three = User.query.offset(3).all()

# Counting records
num_of_users = User.query.count()

print(num_of_users)
