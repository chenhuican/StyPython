#coding:utf-8
from functools import wraps
from flask import session,redirect,url_for

#登录装饰器,判断用户是否登录处理
def login_required(func):
	@wraps(func)
	def wrapper(*args,**kwargs):
		if session.get('user_id'):
			return func(*args,**kwargs)
		else:
			return redirect(url_for('login'))
	return wrapper