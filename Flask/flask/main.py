# Integrating HTML Files with flask

from flask import Flask,render_template
app=Flask(__name__)

@app.route('/index')
def index():
    return '<html><h1>This is an HTML Tag</h1></html>'

# For rendering page need render_template using this we can render to html page it will go and find this in template folder html pages need to create in template folder
@app.route('/htmlPage')
def html_page():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')
@app.route('/')
def root():
    return "root page"
if __name__=='__main__':
    app.run(debug=True)