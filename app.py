from flask import Flask, render_template,jsonify

app = Flask(__name__)

@app.route('/act')
def action():
    return 'Hello there!'

JOBS=[
    {
       'id':1,
       'title':'Data Analyst',
       'Location':'Bengaluru,India',
       'salary':'Rs. 10,00,000'
    },
    {
       'id':2,
       'title':'Data Scienst',
       'Location':'New delhi,India',
       'salary':'Rs. 12,00,000'
    },
    {
       'id':3,
       'title':'Backend Engineer',
       'Location':'Remote',
       'salary':'Rs. 30,00,000'
    },
    {
       'id':4,
       'title':'Frontend Engineer',
       'Location':'Pune,India',
       'salary':'Rs. 23,00,000'
    }
    
]
@app.route('/')
def hello_world():
    return render_template('home.html',jobs=JOBS)
@app.route("/jobs")
def list_jobs():
    return jsonify(JOBS)

if __name__ == '__main__':
    app.run(debug=True)
