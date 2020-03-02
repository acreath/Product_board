from flask import Flask
from flask import make_response


app = Flask(__name__)

@app.route('/')
def index():
    json = {
        "product":"product_board",
        "product manager":"Sky"
    }
    response = make_response(json)
    return response

if __name__ == '__main__':
    app.run(debug=True)