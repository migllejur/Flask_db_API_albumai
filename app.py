from models import db, Albumai
from flask import Flask, jsonify, render_template
from serializers import AlbumasSchema
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///albumai.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
with app.app_context():
    db.create_all()


@app.route("/api/albumai")
def api_albumai():
    all_albums = Albumai.query.all()
    albums_data = [{
        "id": album.id,
        "atlikejas": album.atlikejas,
        "pavadinimas": album.pavadinimas,
        "metai": album.metai,
        "zanras": album.zanras,
        "vidutine_kaina": album.kainu_vidurkis
    } for album in all_albums]
    return jsonify(albums_data)


@app.route("/api2/albumai")
def api2_albumai():
    all_albums = Albumai.query.all()
    albums_data = [AlbumasSchema.model_validate(album).model_dump() for album in all_albums]
    return jsonify(albums_data)


@app.route("/frontend")
def frontend():
    return render_template("albumai.html")


if __name__ == "__main__":
    app.run()
