from flask import Blueprint

jobs_bp = Blueprint("jobs", __name__)


@jobs_bp.get("/checkhealth")
def checkhealth():
    return "/api/v1/jobs is working", 200


@jobs_bp.post("/schedule")
def schedule_job():
    return "New job created", 200


@jobs_bp.get("/")
def get_all_jobs():
    return "Get all jobs", 200


@jobs_bp.put("/<string:job_id>")
def edit_job(job_id: str):
    return f"Editing the job id: {job_id}", 200


@jobs_bp.delete("/<string:job_id>")
def delete_job(job_id: str):
    return f"Deleting the job id: {job_id}", 200


@jobs_bp.post("/<string:job_id>/retry")
def retry_job(job_id: str):
    return f"Retrying the job id: {job_id}", 200
