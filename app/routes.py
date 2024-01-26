from app import app


@app.route('/notes', methods=['GET'])
def get_notes():
    notes = [
        {
            'id': 1,
            'body': 'This is a note to myself',
            'dateCreated': '2024-01-26T12:00:00Z'
        },
        {
            'id': 2,
            'body': 'This is a note to myself',
            'dateCreated': '2024-01-26T12:00:00Z'
        },
        {
            'id': 3,
            'body': 'This is a note to myself',
            'dateCreated': '2024-01-26T12:00:00Z'
        },
        {
            'id': 4,
            'body': 'This is a note to myself',
            'dateCreated': '2024-01-26T12:00:00Z'
        },
    ]
    return notes