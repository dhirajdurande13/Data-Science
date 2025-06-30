# Building URL Dynamically
# Jinja 2 Template engine

'''
JINJA 2 template engine have multiple ways to read
{{}} : Expressions to print output in HTML
{%...%} : conditions, for loop
{#...#} : This is for comments
'''




from flask import Flask,render_template,request,redirect,url_for
app=Flask(__name__)

@app.route('/index',methods=['GET'])
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


#variable rule
@app.route('/success/<int:score>',)
def success(score):
    # return f'The score you got is {score}'
    # return 'The score you got is'+str(score)  #This is known as variable access
    res=""
    if score>50 and score <=80:
        res="PASS"
    elif score>80:
        res="Ditinction"
    else:
        res="FAIL"
    return render_template('result.html',results=res)




@app.route('/success_res/<int:score>',)
def success_res(score):
    # return f'The score you got is {score}'
    # return 'The score you got is'+str(score)  #This is known as variable access
    res=""
    if score>50 and score <=80:
        res="PASS"
    elif score>80:
        res="Ditinction"
    else:
        res="FAIL"
    exp={'Result':res,'Score':score}
    return render_template('result1.html',results=exp)




@app.route('/submit_marks',methods=['POST','GET'])
def submit_marks():
    total_score=''
    if request.method=='POST':
        subject1=float(request.form.get('subject1'))
        subject2=float(request.form.get('subject2'))
        subject3=float(request.form['subject3'])
        subject4=float(request.form['subject4'])
        print(subject1,subject2,subject3,subject4)
    # return render_template('subject.html')
    total_score=(subject1+subject2+subject3+subject4)/4
    # redirect will redirect on specific url
    # And url_for will build dynamic url 
    return redirect(url_for('success_res',score=total_score))


@app.route('/')
def root():
    return "root page"
if __name__=='__main__':
    app.run(debug=True)