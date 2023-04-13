from flask import Flask, render_template, jsonify
from sqlalchemy import text
from databases import engine

app = Flask(__name__)

def load_jobs_from_db():
    jobs = [] 
    with engine.connect() as conn:
        result = conn.execute(text("select * from jobs"))
        
        for row in result.all():
            jobs.append(row._asdict())
        
    return jobs

@app.route("/")
def hello_k():
    jobs_list = load_jobs_from_db()
    return render_template("home.html", jobs=jobs_list)

@app.route("/api/jobs")
def list_jobs():
    return jsonify(JOBS)

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
