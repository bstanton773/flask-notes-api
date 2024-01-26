from app import app, db
from app.models import Note


@app.route('/notes', methods=['GET'])
def get_notes():
    notes = db.session.execute(db.select(Note)).scalars().all()
    return [n.to_dict() for n in notes]