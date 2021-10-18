from flask import Flask, render_template, request
from werkzeug.utils import secure_filename
from werkzeug.datastructures import  FileStorage
from flask import Flask, render_template, request, url_for, jsonify
import json
from flask_cors import CORS, cross_origin
from predict import *

app = Flask(__name__)


@app.route('/getSensorData')
def getSensorData():
    f = open('sensorData.json',)
    data = json.load(f)
    f.close()
    return jsonify(data)

@app.route('/updateData',methods=['POST','OPTIONS'])
def updateData():
    input_json = request.get_json(force=True) 
    f = open("sensorData.json", "w")
    json_object = json.dumps(input_json, indent = 4)
    f.write(json_object)
    f.close() 
    return jsonify(status="true")

@app.route('/')
def test_page():
    example_embed='Sending data... [this is text from python]'
    return render_template('graphs.html', embed=example_embed)

@app.route('/predict')
def predict_activity():
    op = predict_activity_class()
    return (op)
		
if __name__ == '__main__':
   app.run(host='192.168.1.25', port=80)