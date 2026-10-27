
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

jobs = []

@app.route("/")
def home():
    return render_template("index.html", total=len(jobs))

@app.route("/add", methods=["GET", "POST"])
def add_job():
    if request.method == "POST":
        company = request.form["company"]
        role = request.form["role"]
        status = request.form["status"]

        jobs.append({
            "company": company,
            "role": role,
            "status": status
        })

        return redirect(url_for("view_jobs"))

    return render_template("add_job.html")

@app.route("/jobs")
def view_jobs():
    return render_template("jobs.html", jobs=jobs)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
