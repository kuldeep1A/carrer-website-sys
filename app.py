from flask import Flask, render_template, jsonify
<<<<<<< HEAD
from databases import load_jobs_from_db

app = Flask(__name__)

=======

app = Flask(__name__)
JOBS = [
    {   
        'id': 1,
        'title': 'Data Analyst',
        'location': 'Bengaluru, India',
        'salary': 'Rs. 10,00,000'
    },
    {   
        'id': 2,
        'title': 'Data Scientist',
        'location': 'Delhi , India',
        'salary': 'Rs. 15,00,000'
    },
    {   
        'id': 3,
        'title': 'Frontend Engineer',
        'location': 'Remote',
        'salary': 'Rs. 12,00,000'
    },
    {   
        'id': 5,
        'title': 'Backend Engineer',
        'location': 'San Francisco, USA',
        'salary': '$ 120,000'
    }
]
>>>>>>> parent of df78249 (add sqlalchemy to databases)
@app.route("/")
def hello_k():
    return render_template("home.html", jobs=JOBS)

@app.route("/api/jobs")
def list_jobs():
    jobs_list = load_jobs_from_db()
    return jsonify(jobs_list)

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
