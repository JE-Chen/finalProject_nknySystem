import json

from flask import Blueprint, jsonify
from flask_cors import cross_origin

Test = Blueprint('Test', __name__)

Data = [
    {
        'test_name': 'Test Name',
        'test_data': 'Test Data',
        'test_key': 'test_Value'
    }
]


@Test.route(r'/Test_Data')
@cross_origin()
def test_data():
    return jsonify({'Data': Data})


@Test.route(r'/Test_Data/<data_name>')
@cross_origin()
def test_data_with_name(data_name):
    if Data[0].get(data_name) is not None:
        return json.dumps(Data[0][data_name])
    else:
        return '無此值'
