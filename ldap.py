from hashlib import md5
from binascii import b2a_base64
from ldap3 import Server, Connection

server = Server ('ldap://192.168.0.200:389')
ldap = Connection(server, 'cn=admin,dc=dexter,dc=com,dc=br', '4linux')
ldap.bind()

senha = b2a_base64(md5('123'.encode('utf-8')).digest()).decode('utf-8')

user = {
	'cn': 'Thiago',
	'sn': 'souza',
	'mail' : 'thiago448@gmail.com',
	'uid' : '1',
	'userPassword' : '{MD5}' + senha 
}

objectClass = ['top', 'person', 'organizationalPerson', 'inetOrgPerson']
dn = 'mail=' + user['mail'] + ',dc=dexter,dc=com,dc=br'
print(ldap.add(dn, objectClass, user))