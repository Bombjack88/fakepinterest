#ficheiro que cria a base de dados, depois não vai ser mais preciso

from fakepinterest import database, app
from fakepinterest.models import Usuario, Foto

with app.app_context():
    database.create_all()



