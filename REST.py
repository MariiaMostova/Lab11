from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import os
from models.Costumer import Costumer
from models.Clothes import Clothes
from models.Style import Style

basedir = os.path.abspath(os.path.dirname(__file__))
app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'crud.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
ma = Marshmallow(app)

class Costumer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String)
    last_name = db.Column(db.String)
    profession = db.Column(db.String)
    deegre = db.Column(db.Boolean)
    work_experience = db.Column(db.Integer)
    created_documental_films = db.Column(db.Integer)
    wish_salary = db.Column(db.Integer)
    clothes = db.Column(db.Integer)
    style = db.Column(db.Integer)

    def __init__(self, first_name = None, last_name = None, profession = None, deegre = True,
                 work_experience = 0, created_documental_films = 0, wish_salary = 0, clothes = 0, style = 0):
        self.first_name = first_name
        self.last_name = last_name
        self.profession = profession
        self.deegre = deegre
        self.work_experience = work_experience
        self.created_documental_films = created_documental_films
        self.wish_salary = wish_salary
        self.clothes = clothes
        self.style = style

class CostumerSchema(ma.Schema):
    class Meta:
        fields = ('id', 'first_name', 'last_name', 'profession', 'deegre', 'work_experience',
                  'created_documental_films', 'wish_salary', 'clothes', 'style')

costumer_schema = CostumerSchema()
costumers_schema = CostumerSchema(many=True)
db.create_all()

@app.route("/costumer", methods=["POST"])
def add_costumer():
    first_name = request.json['first_name']
    last_name = request.json['last_name']
    profession = request.json['profession']
    deegre = request.json['deegre']
    work_experience = request.json['work_experience']
    created_documental_films = request.json['created_documental_films']
    wish_salary = request.json['wish_salary']
    clothes = request.json['clothes']
    style = request.json['style']
    
    new_costumer = Costumer(first_name, last_name, profession, deegre,
                 work_experience, created_documental_films, wish_salary, clothes, style)

    db.session.add(new_costumer)
    db.session.commit()

    return costumer_schema.jsonify(new_costumer)

@app.route("/costumer", methods=["GET"])
def get_costumer():
    all_costumers = Costumer.query.all()
    result = costumers_schema.dump(all_costumers)
    return jsonify(result.data)

@app.route("/costumer/<id>", methods=["GET"])
def costumer_detail(id):
    costumer = Costumer.query.get(id)
    return costumer_schema.jsonify(costumer)

@app.route("/costumer/<id>", methods=["PUT"])
def costumer_update(id):
    costumer = Costumer.query.get(id)
    first_name = request.json['first_name']
    last_name = request.json['last_name']
    profession = request.json['profession']
    deegre = request.json['deegre']
    work_experience = request.json['work_experience']
    created_documental_films = request.json['created_documental_films']
    wish_salary = request.json['wish_salary']
    clothes = request.json['clothes']
    style = request.json['style']

    costumer.first_name = first_name
    costumer.last_name = last_name
    costumer.profession = profession
    costumer.deegre = deegre
    costumer.work_experience = work_experience
    costumer.created_documental_films = created_documental_films
    costumer.wish_salary = wish_salary
    costumer.clothes = clothes
    costumer.style = style

    db.session.commit()
    return costumer_schema.jsonify(costumer)

@app.route("/costumer/<id>", methods=["DELETE"])
def costumer_delete(id):
    costumer = Costumer.query.get(id)
    db.session.delete(costumer)
    db.session.commit()

    return costumer_schema.jsonify(costumer)


if __name__ == '__main__':
    app.run(debug=True)
