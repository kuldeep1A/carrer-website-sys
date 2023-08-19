import os
from sqlalchemy import create_engine, text
from dotenv import load_dotenv

load_dotenv()


HOST= os.getenv("HOST")
USERNAME= os.getenv("USERNAMEs")
PASSWORD= os.getenv("PASSWORD")
DATABASE= os.getenv("DATABASE")


#  i am using secret key in over program
db_conn_string = f"mysql+pymysql://{USERNAME}:{PASSWORD}@{HOST}/{DATABASE}?charset=utf8mb4"
# print(db_conn_string)

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

j = load_jobs_from_db()
print(j)

