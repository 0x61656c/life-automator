import flask
import data
import functions

app = flask.Flask(__name__)

@app.route('/', methods = ["POST", "GET"])
def index():
    response = {
        "connection" : "Success"
    }

    return flask.jsonify(response)

@app.route('/about', methods = ["POST", "GET"])
def about():
    response = {
        "connection" : "Success",
        "response" : "This application was developed by @ Aaron Lebel to build off of siri shortcuts' ability to make http requests."
    }
    return flask.jsonify(response)

@app.route('/truetime_home_inbound', methods = ["POST", "GET"])
def truetime_home_inbound():
    _truetime = data.get_truetime_home_inbound()
    try:
        response_string = "The inbound truetime from home is currently %s minutes" %(_truetime)
    except:
        response_string = "Something went wrong, and I couldn't get the true time. I'll try again soon."

    response = {
        "connection" : "Success",
        "response" : response_string
    }
    return flask.jsonify(response)

@app.route('/truetime_home_outbound', methods = ["POST", "GET"])
def truetime_home_outbound():
    _truetime = data.get_truetime_home_outbound()
    response = {
        "connection" : "Success",
        "response" : "The outbound truetime from home is currently %s minutes" %(_truetime)
    }
    return flask.jsonify(response)

@app.route('/get_info', methods = ["POST"])
def get_info():
    _input = flask.request.form["input"]
    _data = data.get_information(_input)
    response = {
        "connection" : "Success",
        "response" : str(_data)
    }
    return flask.jsonify(response)

def main():
    app.run(debug = True)

if __name__ == "__main__":
    main()