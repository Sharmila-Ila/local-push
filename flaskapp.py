from flask import Flask,jsonify, render_template
from datetime import datetime
app = Flask(__name__)

@app.route('/')
def test():
    return 'Hello World!'

@app.route('/api')
def index():
    return jsonify({'name': 'Raj',
                   'email': 'raj@outlook.com'})

@app.route('/hello1')
def hello1():
    return render_template(
        "hello.html"  
    )

if __name__=='__main__':
    app.run()