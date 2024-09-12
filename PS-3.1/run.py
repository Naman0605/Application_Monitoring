from flask import Flask

app = Flask(__name__)


@app.get("/")
def index():
    return "Hello, World from the Chrono-AI", 200


if __name__ == "__main__":
    app.run(debug=True, port=8080)
