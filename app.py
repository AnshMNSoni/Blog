from flask import Flask, render_template
from datetime import datetime


app = Flask(__name__)


# Home Page:
@app.route('/')
def homepage():
    year = datetime.now().year
    return render_template('index.html', yr=year)


# Blog on Quantum Computing:
@app.route('/QuantumComputing')
def quantum_computing():
    year = datetime.now().year
    return render_template('quantum_blog.html', yr=year)


# Blog on Elections:
@app.route('/Elections')
def elections():
    year = datetime.now().year
    return render_template('election.html', yr=year)



if __name__ == '__main__':
    app.run(debug=True)
    