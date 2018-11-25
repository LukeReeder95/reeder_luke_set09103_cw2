from flask import Flask, g
import sqlite3
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

app = Flask(__name__)
app.config.from_object(Config)
db_location = 'var/cw.db'
alchDB = SQLAlchemy(app)
login = LoginManager(app)

from app import routes, models
# from app import models

def get_db():
    db = getattr(g, 'db', None)
    if db is None:
        db = sqlite3.connect(db_location)
        g.db = db
    return db

@app.teardown_appcontext
def close_db_connection(exception):
    db = getattr(g, 'db', None)
    if db is not None:
        db.close()

class Driver:
    def __init__(self, name, desc):
        self.name = name
        self.desc = desc

class Blade:
    def __init__(self, role, name, element, weapon, desc):
        self.role = role
        self.name = name
        self.element = element
        self.weapon = weapon
        self.desc = desc

# class User(alchDB.Model, UserMixin):
#     id = alchDB.Column(alchDB.Integer, primary_key=True)
#     username = alchDB.Column(alchDB.String(64), index=True, unique =True)
#     password_hash = alchDB.column(alchDB.String(128))
#
#     def __repr__(self):
#         return '<User {}'.format(self.username)
#
#     def set_password(self, password):
#         self.password.hash = generate_password_hash(password)
#
#     def check_password(self, password):
#         return check_password_hash(self.password_hash, password)

# @app.route('/')
# def index ():
#     db = get_db()
#     test = Driver("Rex", "Test driver")
#
#     return render_template('home.html')
#
# @app.route('/login', methods=['GET', 'POST'])
# def login():
#     if current_user.is_authenticated:
#         return redirect(url_for('index'))
#     form = LoginForm()
#     if form.validate_on_submit():
#         user = User.query.filter_by(username=form.username.data).first()
#         if user is None or not user.check_password(form.password.data):
#             flash('Invalid username or password')
#             return redirect(url_for('login'))
#         login_user(user, remember=form.remember.me.data)
#         return redirect('index')
#     return render_template('login.html', title='Sign In', form=form)
#
# @app.route('/logout')
# def logout():
#     logout_user()
#     return redirect(url_for('index'))
#
# @app.route('/register', methods=['GET', 'POST'])
# def register():
#     if current_user.is_authenticated:
#         return redirect(url_for('index'))
#     form = RegisterForm()
#     if form.validate_on_submit():
#         user = User(username=form.username.data)
#         user.set_password(form.password.data)
#         alchDB.session.add(user)
#         alchDB.session.commit()
#         flash('Successful registration! Also well done, you didnt fuck up the code for this part at long last :^)')
#         return redirect('/')
#     return render_template('register.html', title='Register', form=form)
#
# @app.route('/drivers')
# def drivers():
#     drivernames = []
#     db = get_db()
#     sql = "SELECT name FROM drivers"
#     for row in db.cursor().execute(sql):
#         drivernames.append(row[0])
#
#     return render_template('driverList.html', names=drivernames)
#
# @app.route('/drivers/<drivername>')
# def drivername(drivername):
#     db = get_db()
#     sql = "SELECT * FROM drivers WHERE name=:name"
#     result = db.cursor().execute(sql, {"name":drivername}).fetchone()
#     thisDriver = Driver(result[0], result[1])
#
#     return render_template('DriverDesc.html', driver=thisDriver)
#
#
# @app.route('/blades')
# def blades():
#     bladenames = []
#     db = get_db()
#     sql = "SELECT name FROM blades"
#     for row in db.cursor().execute(sql):
#         bladenames.append(row[0])
#
#     return render_template('bladenames.html', names=bladenames)
#
#
# @app.route('/blades/<bladename>')
# def blade_name(bladename):
#     db = get_db()
#     sql = "SELECT * FROM blades WHERE name=:name"
#     result = db.cursor().execute(sql, {"name":bladename}).fetchone()
#     thisBlade = Blade(result[0], result[1], result[2], result[3], result[4])
#
#     return render_template('BladeDesc.html', blade=thisBlade)
#
# @app.route('/blades/roles')
# def roles():
#     roles = set()
#     db = get_db()
#     sql = "SELECT role FROM blades"
#     for row in db.cursor().execute(sql):
#         roles.add(row[0])
#
#     return render_template("roleList.html", names=roles)
#
# @app.route('/blades/roles/<role>')
# def rolelist(role):
#     blades = []
#     db = get_db()
#     sql = "SELECT name FROM blades WHERE role=:role"
#     result = db.cursor().execute(sql, {"role": role })
#     for row in result:
#         blades.append(row[0])
#
#     return render_template("bladenames.html", names=blades)
#
# @app.route('/blades/weapons')
# def weapons():
#     weapon = set()
#     db = get_db()
#     sql = "SELECT weapon FROM blades"
#     for row in db.cursor().execute(sql):
#         weapon.add(row[0])
#
#     return render_template("weaponList.html", names=weapon)
#
# @app.route('/blades/weapons/<weapon>')
# def weaponlist(weapon):
#     blades = []
#     db = get_db()
#     sql = "SELECT name FROM blades WHERE weapon=:weapon"
#     result = db.cursor().execute(sql, {"weapon": weapon })
#     for row in result:
#         blades.append(row[0])
#
#     return render_template("bladenames.html", names=blades)
#
#
# @app.route('/blades/element')
# def element():
#     elements = set()
#     db = get_db()
#     sql = "SELECT element FROM blades"
#     for row in db.cursor().execute(sql):
#         elements.add(row[0])
#
#     return render_template("elementList.html", names=elements)
#
# @app.route('/blades/element/<element>')
# def elementlist(element):
#     blades = []
#     db = get_db()
#     sql = "SELECT name FROM blades WHERE element=:element"
#     result = db.cursor().execute(sql, {"element": element })
#     for row in result:
#         blades.append(row[0])
#
#     return render_template("bladenames.html", names=blades)
#
# @app.route('/send', methods=['GET', 'POST'])
# def send():
#     if request.method == 'POST':
#         bladeName = request.form['bladename']
#         bladeRole = request.form['role']
#         bladeElement = request.form['element']
#         bladeWeapon = request.form['weapon']
#         bladeDesc = request.form['description']
#         print(bladeName, bladeRole, bladeElement, bladeWeapon, bladeDesc)
#
#
#         db = get_db()
#         sql = "INSERT INTO blades VALUES(?,?,?,?,?)"
#         db.cursor().execute(sql,(bladeRole, bladeName, bladeElement, bladeWeapon, bladeDesc))
#         db.commit()
#
#
#
#         return redirect(url_for('index'))
#
#     return render_template('input.html')
