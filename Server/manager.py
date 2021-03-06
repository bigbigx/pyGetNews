# -*-coding:utf-8 -*-  
from flask.ext.script import Manager, Server 
from api import app, db, User 

manager = Manager(app)

manager.add_command('server',Server())

@manager.shell
def make_shell_context():
	return dict(app=app,db=db,User=User)
	
if __name__ == '__main__':
	manager.run()