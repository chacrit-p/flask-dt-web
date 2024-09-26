from flask import Flask, render_template
from const import (
    APP_HOST,
    APP_DEBUG_MODE,
    APP_PORT,
    APP_TEMPLATE_FOLDER,
    APP_STATIC_FOLDER,
    APP_STATIC_URL_PATH,
)

app = Flask(
    __name__,
    template_folder=APP_TEMPLATE_FOLDER,
    static_folder=APP_STATIC_FOLDER,
    static_url_path=APP_STATIC_URL_PATH,
)


@app.route("/")
def index():
    return render_template("index.html")


if __name__ == "__main__":
    app.run(host=APP_HOST, debug=APP_DEBUG_MODE, port=APP_PORT)
