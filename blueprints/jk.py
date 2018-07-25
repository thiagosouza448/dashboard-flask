#!/usr/bin/python3
import jenkins
from flask import Blueprint, render_template, redirect, session


jk = Blueprint ('jk', __name__ , url_prefix='/jenkins')
jc = jenkins.Jenkins('http://192.168.0.200:8080')


@jk.route('')
def home():
	if not session.get('auth'):
		return redirect ('/')
	for job in jc.get_jobs():
		if job ['name'] == 'Pipiline':
			pipiline= job
			break
	else:
		pipiline = {'name': 'Nenhum job encontrado', 'color' : ''}
	pipiline ['color'] = 'construiu' if pipiline['color'] == 'blue' else 'falhou'
	return render_template('jenkins.html', job=pipiline )









#sudo apt-get install python3-jenkins