from sqlalchemy import create_engine

db_conn_string = "mysql+pymysql://pgi0lvar9ob7uq60gesa:pscale_pw_MSwMiGIPmiLzUcYMXOGuc6QYg3HEH6VMzmx8XKb7irv@aws.connect.psdb.cloud/career_website?charset=utf8mb4"

engine = create_engine(
    db_conn_string,
    connect_args={
        "ssl": {
            "ssl_ca": "/etc/ssl/cert.pem"
        }
    }
) 
# jobs = []

# with engine.connect() as conn:
#     result = conn.execute(text("select * from jobs"))
#     for row in result.all():
#         jobs.append(row._asdict())
    

# print(jobs)