#!/usr/bin/env python
#coding:utf-8

from flask import Flask,jsonify,render_template,request
app = Flask(__name__)

@app.route('/_add_numbers')
def add_numbers():
	a = request.args.get('a',0,type=int)
	b = request.args.get('b',0,type=int)

	return jsonify(result=a+b)

@app.route('/')
def index():
	return render_template('index.html')


if __name__ == '__main__':
	app.run()

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session,sessionmaker
db_connect_string ='mysql://vuser:vpassword@localhost:3306/test_db?charset=utf-8'

ssl_args ={
	'ssl':{
	'cert':'/home/ssl/client-cert.pem',
	'key':'/home/ssl/client-key.pem',
	'ca':'/home/ssl/ca-cert.pem'
	}
}
engine = create_engine(db_connect_string,connect_args=ssl_args)

SessionType = scoped_session(sessionmaker(bind=engine,expire_on_commit=False))

def get_session():
	return SessionType()

from contextlib import contextmanager
@contextmanager
def session_scope():
	session = get_session()
	try:
		yied session
		session.commit()
	except:
		session.rollback()
		raise
	finally:
		session.close()

#进行数据库操作的代码

import orm
from sqlalchemy import _or
#新增操作
def insertaccount(user,password,title,salary):
	with session_scope() as session:
		account = orm.Account(user_name=user,password=password,title=title,salary=salary)
		session.add(account)
#查询操作
def getaccount(id=None,user_name=None):
	with session_scope() as session:
		return session.query(orm.Account).filter(
			or_(orm.Accout.id==id,orm.Account.user_name==user_name)).first()

#删除操作
def deleteaccount():
	with session_scope() as session:
		account = getaccount(user_name=user_name)
		if account:
			session.delete(account)

#更新操作
def updateaccount(id,user_name,password,title,salary):
	with session_scope() as session:
		account = session.query(orm.Account).filter(orm.Account.id == id).first()
		if not account:return
		account.user_name= user_name
		account.password = password
		account.title = title
		account.salary = salary
