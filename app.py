from flask import Flask
from models import db, User, Role, Permission

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///rbac.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

# IMPORTANT: everything inside app context
with app.app_context():
    db.create_all()

    if not Role.query.first():
        read = Permission(name='read')
        write = Permission(name='write')
        delete = Permission(name='delete')

        admin = Role(name='Admin', permissions=[read, write, delete])
        editor = Role(name='Editor', permissions=[read, write])
        viewer = Role(name='Viewer', permissions=[read])

        alice = User(username='Alice', role=admin)
        bob = User(username='Bob', role=editor)
        eve = User(username='Eve', role=viewer)

        db.session.add_all([read, write, delete, admin, editor, viewer, alice, bob, eve])
        db.session.commit()

        print("Database created!")

from routes import *

if __name__ == "__main__":
    app.run(debug=True)