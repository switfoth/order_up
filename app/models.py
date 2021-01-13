from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

db = SQLAlchemy()

class Employee(db.Model, UserMixin):
    id = Column(Integer, primary_key = True)
    name = Column(String(100))
    employee_number = Column(Integer)
    hashed_password = Column(String(100))
    __table_args__= UniqueConstraint('employee_number')

@property
def password(self):
    return self.hashed_password

@password.setter
def password(self, password):
    self.hashed_password = generate_password_hash(password)

def check_password(self, password):
    return check_password_hash(self.password, password)
