

from flask import Flask,render_template,request
app=Flask(__name__)

@app.route('/index',methods=['GET']) #By default it is get method
def index():
    return '<html><h1>This is an HTML Tag</h1></html>'


@app.route('/htmlPage')
def html_page():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

# Handaling get and post at a time for form
# We have to use request.form when we work with POST MEthod and will use request.args when have to work with GET Method
@app.route('/form',methods=['GET','POST'])
def form_api():
    if request.method=='POST':
        fname=request.form.get('fname')
        lname=request.form.get('lname')
        print(fname,lname)
        return f'<html><h3>Name: {fname}</h3><h3>LNAme: {lname}</h3></html>'
    return render_template('form.html')



@app.route('/form_action',methods=['GET','POST'])
def form_action():
    if request.method=='POST':
        fname=request.form.get('fname')
        lname=request.form.get('lname')
        print(fname,lname)
        return f'<html><h3>Name: {fname}</h3><h3>LNAme: {lname}</h3> <p>Using action</p></html>'
    return render_template('form.html')




@app.route('/')
def root():
    return "root page"
if __name__=='__main__':
    app.run(debug=True)