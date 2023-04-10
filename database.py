from sqlalchemy import create_engine,text

connection_string = "mysql+mysqlconnector://flx6b27x89qsg14htz91:pscale_pw_WnqokiRrVgfRa0n7yYMrrY8lzu8XrnTBCN0lUT6vkKu@aws.connect.psdb.cloud:3306/minprojectscandance"

engine = create_engine(connection_string, echo=True)
with engine.connect() as connection:
  result = connection.execute(text("SELECT * FROM stud_attendance;"))
studrec = []
for row in result.mappings():
    studrec.append(dict(row))

print(studrec,"\n")