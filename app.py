from flask import Flask,render_template, jsonify

app = Flask(__name__)

@app.route("/studrec")
def hello_world():
  return render_template('registerpage.html')

@app.route("/")
def hello():
  return render_template('studentrecord.html',Studentrec = stud_rec)


@app.route("/jsonstuderec")
def studentlist():
  return jsonify(stud_rec)

stud_rec = [
  {
    'prn'  : 1,
    'name' :'Jack',
    'count': 10
  },
  {
    'prn'  : 2,
    'name' :'Jackie',
    'count': 11
    },
  {
    'prn'  : 3,
    'name' :'Jacob',
    'count': 9
    }
]

if __name__ == "__main__":
  app.run(host='0.0.0.0',debug=True)