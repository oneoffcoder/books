from flask import Flask, jsonify, request
from flask_cors import CORS
import json
import time
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import mysql
from bo import Student

app = Flask(__name__)
app.config.from_object('config')
CORS(app, resources={r'/*': {'origin': '*'}})

connect_args = {
    'ssl_disabled': 'True'
}

engine = create_engine(
    f'mysql+mysqlconnector://{app.config["DB_USER"]}:{app.config["DB_PW"]}@{app.config["DB_HOST"]}:{app.config["DB_PORT"]}/{app.config["DB_INSTANCE"]}', 
    isolation_level='AUTOCOMMIT',
    connect_args=connect_args,
    echo=True)
Session = sessionmaker(bind=engine)
session = Session()

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
    return json.dumps({'message': app.config['AUTHOR']})


@app.route('/v1/test', methods=['GET'])
def hello():
    current_milli_time = lambda: int(round(time.time() * 1000))
    return json.dumps({
        'author': app.config['AUTHOR'],
        'app_name': app.config['APP_NAME'],
        'timestamp': current_milli_time()
    })

@app.route('/v1/student', methods=['POST'])
def create():
    j = request.json
    s = Student.instance(j['first_name'], j['last_name'], j['gender'])
    session.add(s)
    return json.dumps({'message': 'OK'})

@app.route('/v1/student/<id>', methods=['GET'])
def read(id):
    student = session.query(Student).filter_by(id=id).first()
    if student is None:
        return json.dumps({'message': f'no such id {id}'})
    return json.dumps(student.dict())

@app.route('/v1/students', methods=['GET'])
def read_all():
    students = session.query(Student)
    students = [s.dict() for s in students]
    return json.dumps(students)

@app.route('/v1/student/<id>', methods=['PUT'])
def update(id):
    student = session.query(Student).filter_by(id=id).first()
    if student is not None:
        j = request.json
        student.first_name = j['first_name']
        student.last_name = j['last_name']
        student.gender = j['gender']
        session.commit()
        return json.dumps({'message': 'OK'})
    else:
        return json.dumps({'message': f'no such id {id}'})

@app.route('/v1/student/<id>', methods=['DELETE'])
def delete(id):
    student = session.query(Student).filter_by(id=id).first()
    if student is not None:
        session.delete(student)
        return json.dumps({'message': 'OK'})
    return json.dumps({'message': f'no such id {id}'})


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')