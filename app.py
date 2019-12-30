#!/usr/bin/python3
import logging
from hashlib import md5
from binascii import b2a_base64
from ldap3 import Server, Connection
from flask import Flask, render_template, request, session, redirect

from blueprints.pocker import pocker
# from blueprints.jk import jk
from blueprints.gitlab import gitlab

app = Flask (__name__)
app.secret_key = '	'
# app.register_blueprint(jk)
app.register_blueprint(pocker)
app.register_blueprint(gitlab)

logging.basicConfig(
	filename= 'app.log',
	level=logging.WARNING,
	format= '%(asctime)s [ %(levelname)s] %(name)s [%(funcName)s] [%(filename)s, %(lineno)s %(message)s' ,
	datefmt= '[%d/%m/%y %H:%M:%S]'
)

@app.route('/')
def home():
	logging.error('Acessaram o dashboard')
	if session.get('auth'):
		return redirect ('/docker')
	return render_template ('index.html')

@app.route('/login', methods=['POST'])
def login():
	mail= request.form['email']
	password = request.form['password']
	server = Server ('ldap://192.168.0.200:389')
	ldap = Connection(server, 'mail=' + mail + ',dc=dexter,dc=com,dc=br', password)
	if ldap.bind():
		session['auth'] = True
		return redirect('/docker')
	else:
		logging.warning('autenticação invalida')
		return redirect('/')
	
@app.route('/logoff')
def logoff():
	if session.get('auth'):
		del session['auth']
	return redirect('/')
	



app.run()





#docker run --name flask-app -dti -p 9090:80 flask-app   criar um container para ligar em casa