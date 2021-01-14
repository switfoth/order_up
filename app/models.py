from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

db = SQLAlchemy()


class Employee(db.Model, UserMixin):
    __tablename__ = "employees"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    employee_number = db.Column(db.Integer, unique=True)
    hashed_password = db.Column(db.String(100))


    @property
    def password(self):
        return self.hashed_password


    @password.setter
    def password(self, password):
        self.hashed_password = generate_password_hash(password)


    def check_password(self, password):
        return check_password_hash(self.password, password)

class Menu(db.Model):
    __tablename__ = "menus"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30))

class MenuItem(db.Model):
    __tablename__ = "menu_items"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    price = db.Column(db.Float)
    menu_id = db.Column(db.Integer, db.ForeignKey("menus.id"))
    menu_type_id = db.Column(db.Integer, db.ForeignKey("menu_item_types.id"))
    menu = db.relationship("Menu")
    type = db.relationship("MenuItemType")

class MenuItemType(db.Model):
    __tablename__ = "menu_item_types"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20))
