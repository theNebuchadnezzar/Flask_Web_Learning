#!/usr/bin/env python
import os
from bolg_app import creat_app, db
from bolg_app.models import User, Role
from flask.ext.script import  Manager, Shell
from flask.ext.migrate import Migrate, MigrateCommand

blog_app = creat_app(os.getenv('FLASK_CONFIG')or 'default')
manager = Manager(blog_app)
migrate = Migrate(blog_app, db)

def make_shell_context():

    return dict(blog_app = blog_app, db = db, User = User, Role = Role)
manager.add_command("shell", Shell(make_context = make_shell_context))
manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run()

@manager.command
def test():
    """Run the unit tests."""
    import unittest
    tests = unittest.TestLoader().discover('test')
    unittest.TextTestRunner(verbosity=2).run(test)
