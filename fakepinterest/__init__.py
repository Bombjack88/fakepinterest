# importa o flask e cria aplicação

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_bcrypt import Bcrypt
import os


# 1) código das páginas do website -> programa routes.py
app = Flask(__name__)

# 2) código do banco de dados -> programa models.py
app.config["SQLALCHEMY_DATABASE_URI"] =os.getenv("DATABASE_URL")

"sqlite:///comunidade.db"
postgresql://banco_fakepinterest_55kc_user:jr1rEXOstBPnvlPgbq7yVpgjvJynXED9@dpg-crg5q6rqf0us73dhsabg-a/banco_fakepinterest_55kc

database = SQLAlchemy(app)

# 3) código de sistema de login e segurança (gerenciador de passwords)
app.config["SECRET_KEY"] ="e2ba84d02cc5a1b367c3313eb363b4bf"
bcrypt = Bcrypt(app)

login_manager = LoginManager(app)
login_manager.login_view = "homepage"

# 4) código para carregar as fotos

app.config["UPLOAD_FOLDER"] ="static/fotos_post"


# 99) programas que precisam de correr (sempre no final)
from fakepinterest import routes