# server-side app handling HTTP requests from RPi clients
from flask import Flask, request, render_template, flash, url_for, jsonify
import requests
import time

app = Flask(__name__)

# main URL displays welcome page
@app.route("/")
def home():
    return render_template("index.html")

# tests HTTP via entering raw msg
@app.route('/test_http_raw', methods = ["POST","GET"])
def test():
    if request.method == 'GET':
        return f"The URL is accessed directly. Try going to '/test_http_form' to submit form"
    if request.method == 'POST':
        form_data = request.form
        return render_template('data.html',form_data = form_data)

# tests HTTP via entering json msg
@app.route('/test_http_json', methods = ["POST","GET"])
def test():
    if request.method == 'GET':
        return f"The URL is accessed directly (json). Try going to '/test_http_form' to submit form"
    if request.method == 'POST':
        form_data = request.form
        return render_template('data.html',form_data = form_data)

# tests HTTP via user inputs
@app.route('/test_http_form', methods = ["POST","GET"])
def test_json():
    if request.method == 'POST':
        variable_name = request.form.get("variable_name")
        variable_value = request.form.get("variable_value")
        return render_template('data.html',form_data = form_data)


# handles a post request
@app.route('/request_handle_json', methods=['POST','GET'])
def server_process_json_request():
    # get json format request
    input_json = request.get_json(force=True)
    # print parsed data in terminal
    print('data from client:', input_json)
    # process into result ...
    # ...
    # send result in json format
    dictToReturn = {'answer': 42}
    return jsonify(dictToReturn)


if __name__ == '__main__':
    app.run()