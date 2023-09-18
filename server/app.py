#!/usr/bin/env python3

from flask import Flask, make_response, jsonify
from flask_migrate import Migrate

from models import db, Bakery, BakedGood

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.json.compact = False

migrate = Migrate(app, db)

db.init_app(app)

@app.route('/')
def index():
    return '<h1>Bakery GET API</h1>'

@app.route('/bakeries')
def bakeries():
    all_bak = []
    for bak in Bakery.query.all():
        bak_dict = {
            "name": bak.name
        }
        all_bak.append(bak_dict)
    
    response = make_response(
        jsonify(all_bak),
        200
    )
    
    return response

@app.route('/bakeries/<int:bak_id>')
def bakery_by_id(bak_id):
    bak = Bakery.query.filter_by(id=bak_id).first()
    bak_dict = bak.to_dict()
    response = make_response(jsonify(bak_dict), 200)
    response.headers["Content-Type"] = "application/json"
    
    return response

@app.route('/baked_goods/by_price')
def baked_goods_by_price():
    baked_goods = BakedGood.query.order_by(BakedGood.price).all()
    
    response = make_response(jsonify(baked_goods), 200)
    response.headers["Content-Type"] = "application/json"
    return response

@app.route('/baked_goods/most_expensive')
def most_expensive_baked_good():
    return ''

if __name__ == '__main__':
    app.run(port=5555, debug=True)
