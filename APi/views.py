from flask import Flask, jsonify, abort, request, json

import datetime
from models import RedFlagRecord, User

app = Flask(__name__)


redflags = []


@app.route('/api/v1/POST/redflags', methods=['POST'])
def create_redflag():
    if not request.json or not "incidentType" in request.json:
        return jsonify(
            {
                'status': 400,
                'error': 'Use the required format'
            }), 400

    redflagId = len(redflags) + 1
    createdOn = datetime.date.today()

    redflag = {
        "id": redflagId,
        "createdOn": createdOn,
        "createdBy": request.json.get("createdBy", ""),
        "incidentType": request.json["incidentType"],
        "location": request.json.get("location", ""),
        "status": request.json.get("status", ""),
        "images": request.json.get("images", ""),
        "Videos": request.json.get("videos", ""),
        "comment": request.json.get("comment")
    }
    redflags.append(redflag)
    return jsonify({'redflags': redflag, 'status': 201}), 201


if __name__ == '__main__':
    app.run(debug=True)
