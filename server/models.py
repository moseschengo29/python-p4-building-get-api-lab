from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData
from sqlalchemy_serializer import SerializerMixin

metadata = MetaData(naming_convention={
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
})

db = SQLAlchemy(metadata=metadata)

class Bakery(db.Model, SerializerMixin):
    __tablename__ = 'bakeries'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())
    
    baked_goods = db.relationship('BakedGood', backref='baked_goods_bakery')
    
    def __repr__(self):
        return f'{self.name}'

class BakedGood(db.Model, SerializerMixin):
    __tablename__ = 'baked_goods'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    price = db.Column(db.Float)  # Change to Float if price can have decimal values
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())
    
    bakery_id = db.Column(db.Integer, db.ForeignKey('bakeries.id'))
    bakery = db.relationship('Bakery', back_populates='baked_goods', viewonly=True)  # Set viewonly to True
    
    def __repr__(self):
        return f'{self.name} with price {self.price}'

