# server-side app handling HTTP requests from RPi clients
from flask import Flask, request, render_template, flash, jsonify
import json
import time

app = Flask(__name__)

### ---------- Utility functions ----------
# load variables from database
def fetch_database():
    # load json file
    with open('database.json', 'r') as json_file:
        json_load = json.load(json_file)
        json_file.close()
    return json_load

### ---------- Server's endpoints ----------
# main URL displays welcome page
@app.route("/")
def home():
    return render_template("index.html")

# test http requests JSON
@app.route('/test_http_json/', methods = ["POST","GET"])
def test_http_json():
    # ----- retrieve data from server
    if request.method == "GET":
        # load database
        database = fetch_database()
        # OPTIONAL : lookup key of each requested variable
        for var_name in request.args():
            # METHOD1 : iterate through json string
            database_string = json.dumps(database, separators=(',', ':'))
            for string in database_string:
                # TODECIDE do something with the data
                if var_name == string:
                    print(string)
                else:
                    pass
            # METHOD2 : directly find (nested) variable.s
            targeted_data = database['clients']['rpi2']['temperature']
        # show full extracted data
        flash(database)

    # ----- post data to server
    if request.method == "POST":
        # get device ID from header
        device_id = request.headers.get('device_id')
        # load current database
        data = fetch_database()
        # for each variable in request
        for var_name in request.args():
            # replace database variables with their value
            data['clients'][device_id][var_name] = var_name.key()
        # replace database file
        with open('database.json', 'w') as f:
            json.dump(data, f)
            json.close()
        # show full replaced data
        flash(data)

# tests HTTP via user inputs
@app.route('/test_http_json_form/', methods = ["POST"])
def test_http_json_form():
    if request.method == 'POST':
        variable_name = request.form.get("variable_name")
        variable_value = request.form.get("variable_value")
        flash(variable_name, variable_value)
    else:
        flash('POST method only !')

### ----- Launch app -----
if __name__ == '__main__':
    app.run(port=443,debug=True)