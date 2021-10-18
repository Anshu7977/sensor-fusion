from flask import Flask, render_template, request
from werkzeug.utils import secure_filename
from werkzeug.datastructures import  FileStorage
from flask import Flask, render_template, request, url_for, jsonify
import json
from flask_cors import CORS, cross_origin


app = Flask(__name__)
cors = CORS(app)


@app.route('/getSensorData')
@cross_origin()
def upload_file():
    f = open('sensorData.json',)
    data = json.load(f)
    f.close()
    return jsonify(data)

@app.route('/updateData',methods=['POST','OPTIONS'])
@cross_origin()
def bulk_upload_log_folder():
    input_json = request.get_json(force=True) 
    f = open("sensorData.json", "w")
    json_object = json.dumps(input_json, indent = 4)
    f.write(json_object)
    f.close() 
    return jsonify(status="true")

@app.route('/')
@cross_origin()
def test_page():
    example_embed='Sending data... [this is text from python]'
    return render_template('graphs.html', embed=example_embed)

		
if __name__ == '__main__':
   app.run(debug = True)