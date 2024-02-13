# main.py
 
from flask import Flask, render_template, request, jsonify
from typing import Annotated
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import func
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import DeclarativeBase, MappedAsDataclass
from datetime import datetime
import json
from dataclasses import dataclass, asdict
from sqlalchemy import JSON, Integer, String
from flask_migrate import Migrate

 
app = Flask(__name__)
 
# MySql datebase
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://root:@localhost:3306/dbname?charset=utf8"

db = SQLAlchemy(app, disable_autonaming=True)

migrate = Migrate(app, db)

# declarative base class
class Base(DeclarativeBase, MappedAsDataclass):
    pass

class Product(Base):
    __tablename__ = 'product'

    id: Mapped[int] = mapped_column(Integer, primary_key=True, init=False)
    email: Mapped[str] = mapped_column(String(100), unique=True)
 
 
@app.route('/')
def index():
    Base.metadata.create_all(db.get_engine(), Base.metadata.tables.values(), checkfirst=True)


    db.session.add(Product("1@gmail.com"))
    db.session.add(Product("2@gmail.com"))
    db.session.add(Product("3@gmail.com"))

    db.session.commit()
    return "123"
    
@app.route('/a')
def a():
    return db.session.execute(db.select(Product)).scalars().all()
 
if __name__ == "__main__":
    app.run(debug=True)