<<<<<<< HEAD
from sqlalchemy import create_engine

db_conn_string = "mysql+pymysql://pgi0lvar9ob7uq60gesa:pscale_pw_MSwMiGIPmiLzUcYMXOGuc6QYg3HEH6VMzmx8XKb7irv@aws.connect.psdb.cloud/career_website?charset=utf8mb4"
=======
from sqlalchemy import create_engine, text
import os
db_conn_string = os.environ.get["DB_CONNECTION_STRING"]
>>>>>>> 18a1ed1 (chnages)

engine = create_engine(
    db_conn_string,
    connect_args={
        "ssl": {
            "ssl_ca": "/etc/ssl/cert.pem"
        }
    }
) 
def load_jobs_from_db():
    jobs = [] 
    with engine.connect() as conn:
        result = conn.execute(text("select * from jobs"))
        
        for row in result.all():
            jobs.append(row._asdict())
        
    return jobs

