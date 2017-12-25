#coding:utf-8
from flask import Flask, render_template,request,url_for,redirect,session
import config
from exts import db
from models import User,Question,Answer
from decorator import login_required
from sqlalchemy import or_

app = Flask(__name__)
app.config.from_object(config)
db.init_app(app)

@app.route('/')
def index():
	context = {
		'questions':Question.query.order_by(Question.create_time.desc()).all()
	}
	return render_template('index.html',**context)

@app.route('/login/', methods=['GET','POST'])
def login():
	if request.method == 'GET':
		return render_template('login.html')
	else:
		telephone = request.form.get('telephone')
		password  = request.form.get('password')
		user      = User.query.filter(User.telephone==telephone,User.password==password).first()
		if user:
			#用户存在则设置 cookies
			session['user_id'] = user.id
			return redirect(url_for('index'))
		else:
			return u'手机号码或者密码错误，请确认后再输入！'

@app.route('/regist/', methods=['GET','POST'])
def regist():
	if request.method == 'GET':
		return render_template('regist.html')
	else:
		telephone = request.form.get('telephone')
		username  = request.form.get('username')
		password1 = request.form.get('password1')
		password2 = request.form.get('password2')

		#手机号码验证，如果被注册了，就不能再注册了
		user = User.query.filter(User.telephone==telephone).first()
		if user:
			return u'该手机已被注册，请更换手机号码!'
		else:
			if password1 != password2:
				return u'两次输入的密码不相等，请核对后再填写！'
			else:
				user = User(telephone=telephone,username=username,password=password1)
				db.session.add(user)
				db.session.commit()
				return redirect(url_for('login'))

@app.route('/logout/',methods=['GET','POST'])
def logout():
	#session.pop('user_id')
	#del_session('user_id')
	session.clear()
	return redirect(url_for('login'))

@app.route('/question/',methods=['GET','POST'])
@login_required
def question():
	if request.method=='GET':
		return render_template('question.html')
	else:
		title = request.form.get('title')
		content = request.form.get('content')
		question = Question(title=title,content=content)
		user_id = session.get('user_id')
		user = User.query.filter(User.id==user_id).first()
		question.author = user
		db.session.add(question)
		db.session.commit()
		return redirect(url_for('index'))

@app.route('/detail/<question_id>')
def detail(question_id):
	if question_id:
		question_model = Question.query.filter(Question.id==question_id).first()
		return render_template('detail.html',question=question_model)
	else:
		pass

@app.route('/answer/',methods=['POST'])
@login_required
def answer():
	if request.method=='POST':
		content = request.form.get('answer_content')
		answer = Answer(content=content)
		question_id = request.form.get('question_id')
		user_id = session.get('user_id')
		user = User.query.filter(User.id==user_id).first()
		answer.author = user
		question = Question.query.filter(Question.id==question_id).first()
		answer.question = question
		db.session.add(answer)
		db.session.commit()
		return redirect(url_for('detail',question_id=question_id))


@app.route('/search/')
def search():
	cnts = request.args.get('q')
	if cnts:
		questions = Question.query.filter(or_(Question.title.contains(cnts),Question.content.contains(cnts))).order_by(Question.create_time.desc())
		return render_template('index.html',questions=questions)



# 上下文钩子 获取用户，用于页面显示登录用户名
@app.context_processor
def my_context_processor():
	user_id = session.get('user_id')
	if user_id:
		user = User.query.filter(User.id==user_id).first()
		if user:
			return {'user':user}
	return {}

if __name__ == '__main__':
	app.run()