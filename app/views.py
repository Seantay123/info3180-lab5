"""
Flask Documentation:     https://flask.palletsprojects.com/
Jinja2 Documentation:    https://jinja.palletsprojects.com/
Werkzeug Documentation:  https://werkzeug.palletsprojects.com/
"""

from flask import Blueprint, render_template, request, jsonify, send_from_directory
import os
from werkzeug.utils import secure_filename

from .forms import MovieForm
from .models import Movie
from . import db

views = Blueprint('views', __name__)

###
# Routing for your application.
###

@views.route('/')
def index():
    return jsonify(message="This is the beginning of our API")


###
# Helper function
###

def form_errors(form):
    error_messages = []
    for field, errors in form.errors.items():
        for error in errors:
            message = f"Error in the {getattr(form, field).label.text} field - {error}"
            error_messages.append(message)
    return error_messages


UPLOAD_FOLDER = 'app/uploads'


@views.route('/api/v1/movies', methods=['POST'])
def movies():
    data = request.get_json()

    title = data.get('title')
    description = data.get('description')
    poster = data.get('poster')
    
    filename = secure_filename(file.filename)
    file.save(os.path.join(UPLOAD_FOLDER, filename))

    movie = Movie(
        title=title,
        description=description,
        poster=poster
    )

    db.session.add(movie)
    db.session.commit()

    return jsonify({
        "message": "Movie Successfully added",
        "title": title,
        "poster": poster,
        "description": description
    })


@views.route('/api/v1/movies', methods=['GET'])
def get_movies():
    movies = Movie.query.all()

    return jsonify({
         "movies": [
            {
               "id": movie.id,
               "title": movie.title,
               "description": movie.description,
               "poster": f"/api/v1/posters/{movie.poster}"
        }
        for m in movies
        ]
    })

    return jsonify({"movies": movie_list})


@views.route('/api/v1/posters/<filename>')
def get_poster(filename):
    return send_from_directory(UPLOAD_FOLDER, filename)


@views.app_errorhandler(404)
def page_not_found(error):
    return render_template('404.html'), 404