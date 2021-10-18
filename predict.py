import urllib.request
import json

def predict_activity_class():
    f = open('sensorData.json',)
    sensorData = json.load(f)
    f.close()

    data = {
        "data" : [sensorData], "method" : "predict"
    }

    body = str.encode(json.dumps(data))

    url = 'http://47e7a864-80f5-409a-979d-21aa1d4df817.centralindia.azurecontainer.io/score'
    headers = {'Content-Type':'application/json'}

    req = urllib.request.Request(url, body, headers)

    try:
        response = urllib.request.urlopen(req)
        result = response.read()
        my_json = result.decode('utf8').replace("'", '"')
        data = json.loads(my_json)
        s = json.dumps(data, indent=4, sort_keys=True)
        return json.loads(s)
    except urllib.error.HTTPError as error:
        print("The request failed with status code: " + str(error.code))
        print(error.info())
        print(json.loads(error.read().decode("utf8", 'ignore')))