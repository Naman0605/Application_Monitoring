from flask import Blueprint

jobs_bp = Blueprint("jobs", __name__)


@jobs_bp.get("/checkhealth")
def checkhealth():
    return "/api/v1/jobs is working", 200
