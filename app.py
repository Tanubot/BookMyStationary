from flask import Flask,render_template, jsonify
from database import engine
from sqlalchemy import text

stud_rec = []

def load_studrecords_from_db():
  with engine.connect() as conn:
    result = conn.execute(text("SELECT * FROM stud_attendance;"))
    for row in result.mappings():
      stud_rec.append(dict(row))
    return stud_rec


app = Flask(__name__)

@app.route("/studrec")
def hello_world():
  return render_template('registerpage.html')

@app.route("/")
def hello():
  Studentrec = load_studrecords_from_db()
  print(Studentrec)
  return render_template('studentrecord.html',Studentrec =  Studentrec)
  


@app.route("/jsonstuderec")
def studentlist():
  return jsonify(stud_rec)



if __name__ == "__main__":
  app.run(host='0.0.0.0',debug=True)