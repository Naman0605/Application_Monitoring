from flask import Flask

from app.routes.jobs import jobs_bp

app = Flask(__name__)
app.register_blueprint(jobs_bp, url_prefix="/api/v1/jobs")


@app.get("/checkhealth")
def checkhealth():
    return "The api is working", 200


if __name__ == "__main__":
    app.run(debug=True, port=8080)
