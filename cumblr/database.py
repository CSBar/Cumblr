from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def setup_database():
    """
    Setup some initial conditions after clearing database
    """

    from cumblr.models import Role, User

    role_user = Role('user', 'basic user role')
    role_superuser = Role('superuser', 'admin privileges role')

    user_admin = User('admin@cum.blr', 'email')
    user_admin.email = 'admin@cum.blr'
    user_admin.username = 'cumblr'
    user_admin.password = User.hash_password('admin')
    user_admin.roles.extend([role_user, role_superuser])

    db.session.add(role_user)
    db.session.add(role_superuser)
    db.session.add(user_admin)
    db.session.commit()

    print('User and Superuser roles created')
