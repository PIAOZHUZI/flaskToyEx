from flask import Flask, render_template, url_for,request
app = Flask(__name__)
text =""
@app.route('/',methods=['get','post'])
def main():
	if (request.method=='POST'):
		text=request.form['write']
		if(text==None) :
			text=""
	else :
		text=""
	return render_template('form.html',text=text)

@app.route('/')
def hello():
    return render_template('hello.html', title = 'hello jinja', num =1)


@app.route('/login')
def login():
    return 'hello, login'


@app.route('/mother')
def mother():
	title='hello jinja'
	return render_template('mother.html')

@app.route('/child')
def child():
	return render_template('child.html')


if __name__ == '__main__': 
    app.run(debug=True)