#!/usr/bin/python3
from flask import Blueprint, render_template


gitlab = Blueprint ('gitlab', __name__ , url_prefix='/gitlab')

TOKEN= 'VXMbTH5V1QLyYjeUxnNX'
GITLAB = 'http://192.168.0.100/api/v4/{route}?private_token={tk}'

@gitlab.route('')
def home():
	users = requests.get(GITLAB.format(tk = TOKEN, route = 'users'))
	projects = requests.get(GITLAB.format(tk = TOKEN, route = 'projects'))
	return render_template(
		'gitlab.html',
		users= users.json(),
		projects=projects.json())









#sudo apt-get install python3-jenkins