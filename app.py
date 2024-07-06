from flask import Flask, render_template
from datetime import datetime


app = Flask(__name__)

@app.route('/')
def homepage():
    year = datetime.now().year
    return render_template('index.html', yr=year)

@app.route('/QuantumComputing')
def get_blogs():
    year = datetime.now().year
    return render_template('quantum_blog.html', yr=year)

if __name__ == '__main__':
    app.run(debug=True)
    
    
# Script to render templates as static HTML files
with app.app_context():
    homepage_html = render_template('index.html', yr=datetime.now().year)
    with open('static_site/index.html', 'w') as f:
        f.write(homepage_html)

    quantum_blog_html = render_template('quantum_blog.html', yr=datetime.now().year)
    with open('static_site/quantum_blog.html', 'w') as f:
        f.write(quantum_blog_html)