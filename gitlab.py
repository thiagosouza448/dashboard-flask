import requests


TOKEN= 'VXMbTH5V1QLyYjeUxnNX'
GITLAB = 'http://192.168.0.100/api/v4/{route}?private_token={tk}'

response = requests.get(GITLAB.format(tk=TOKEN, route='projects'))
for repository in response.json():
	print ('{} - {}'.format(repository['id'], repository['path']))
exit()


# repository = {'name': 'flask-app'}
# response = requests.post(GITLAB.format(tk=TOKEN), repository)
# # print (response.json())


# response = requests.get(GITLAB.format(tk=TOKEN, route='users'))
# for user in response.json():
# 	print ('{} {}'.format (user['id'], user['name']))


# user = {'email': 'parama@yog.com.br' ,
#         'username' : 'paragananda',
#         'name': 'paramahansa',
#         'password':'1a7as4a4s25as3'}
# response= requests.post(GITLAB.format(tk=TOKEN, route='users'), user)
# print(response.json())

pid = 2
member= {'user_id' : 3, 'access_levei': 40}
response = requests.post(
	'http://192.168.0.100/api/v4/projects/{pid}/members?private_token={tk}'.format(pid = 2, tk= TOKEN),
	 member
)

print(response.json())