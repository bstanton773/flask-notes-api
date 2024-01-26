from flask import request
from app import app, db
from app.models import Note


@app.route('/notes', methods=['GET'])
def get_notes():
    notes = db.session.execute(db.select(Note)).scalars().all()
    return [n.to_dict() for n in notes]


@app.route('/notes', methods=['POST'])
def create_note():
    if not request.is_json:
        return {'error': 'Your request Content-Type must be application/json'}, 400
    data = request.json
    if 'body' not in data:
        return {'error': 'You must have "body" in your request body'}, 400
    new_note = Note(body=data['body'])
    return new_note.to_dict(), 201
