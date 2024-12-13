from flask import Flask,render_template

app = Flask(__name__)

@app.route('/')
def hello_world():
    title = "Sample Flask"
    programming_lang=['Python','Java','c++','c']
    return render_template('index.html',title =title ,programming_lang =programming_lang)
# to run type set FLASK_APP=app.py then flask run

@app.route('/about')
def about():
    title="About Us"
    render_template('about.html',title=title)