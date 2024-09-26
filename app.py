from flask import Flask
from consistent import APP_DEBUG_MODE

app = Flask(__name__)


@app.route("/")
def index():
    return "Hello, World!"


if __name__ == "__main__":
    app.run(debug=APP_DEBUG_MODE)
