from flask import render_template, flash, redirect, request, session, url_for, Flask 
from passlib.hash import sha256_crypt
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)

#Cargar las configuraciones
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://cristianPagan:User1234@localhost/flask_db'
app.secret_key = 'devWebPage'

db = SQLAlchemy(app)

@app.route('/')
def dir():
    return redirect(url_for('login'))

#Iniciar Sesión
@app.route('/login', methods=('GET','POST'))
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        pwd = request.form['password']

        error = None
        
        user = User.query.filter_by(correo_electronico = username).first()
        
        if user == None:
            error = 'Nombre de usuario incorrecto'
        elif not sha256_crypt.verify(pwd, user.password):
            error = 'Contraseña incorrecta'
            
        if error is None: 
            session.clear()
            session['user_id'] = user.id_pk
            session['username'] = user.correo_electronico
            return redirect(url_for('index'))
                    
        flash(error)
        
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('login'))

@app.route("/index")
def index():
    logs_count = Log.query.count()
    logs = Log.query.all()
    logs = list(reversed(logs))
    db.session.commit()
    return render_template('dashboard.html', logs = logs, logs_count = logs_count)

## Models 
class User(db.Model):
    __tablename__ = 'admin'
    id_pk = db.Column(db.Integer, primary_key=True)
    correo_electronico = db.Column(db.String(50))
    password = db.Column(db.Text)

    def __init__(self, correo_electronico, password) -> None:
        self.correo_electronico = correo_electronico
        self.password = password

    def __repr__(self) -> str:
        return f'Email: {self.correo_electronico}'

## Models 
class Log(db.Model):
    __tablename__ = 'actividad_red'
    id_pk = db.Column(db.Integer, primary_key=True)
    user = db.Column(db.String(100))
    destinacion = db.Column(db.String(100))
    internal_ip	= db.Column(db.String(50))
    external_ip	= db.Column(db.String(50))	
    categoria = db.Column(db.String(20))
    accion = db.Column(db.String(50))
    tag	= db.Column(db.String(50))
    fecha_hora = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    
    def __init__(self, id_pk, user, destinacion, internal_ip, external_ip, categoria, accion, tag, fecha_hora) -> None:
        self.id_pk = id_pk
        self.user = user
        self.destinacion = destinacion
        self.internal_ip = internal_ip
        self.external_ip = external_ip
        self.categoria = categoria
        self.accion = accion
        self.tag = tag
        self.fecha_hora = fecha_hora
        
    def __repr__(self) -> str:
        return f'User: {self.user}'    
    
if __name__ == '__main__':
    app.run(host = "127.0.0.1", port = 5000)
    