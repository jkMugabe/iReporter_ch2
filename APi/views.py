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
    return jsonify({'data': redflag, 'status': 201}), 201


@app.route('/api/v1/GET/redflags', methods=['GET'])
def get_redflags():
    if len(redflags) == 0:
        return jsonify({'status': 404,
                        'error': 'No redflag available'}), 404
    return jsonify({'data': redflags,
                    'status': 200}), 200


@app.route('/api/v1/GET/redflags/<int:redflag_id>', methods=['GET'])
def get_redflag(redflag_id):
    redflag = [redflag for redflag in redflags if redflag['id'] == redflag_id]
    if len(redflag) == 0:

        return jsonify(
            {
                'status': 404,
                'error': 'Redflag with that ID is not available'
            }), 404
    return jsonify({'status': 200, 'data': redflag[0]}), 200


@app.route('/api/v1/PUT/redflags/<int:redflag_id>/edit_location', methods=['PUT'])
def update_location(redflag_id):
    redflag = [redflag for redflag in redflags if redflag['id'] == redflag_id]
    if len(redflag) == 0:
        return jsonify({'status': 404,
                        'error': 'No redflag available'}), 404
    if not request.json:
        return jsonify(
            {
                'status': 400,
                'error': 'Use the required format'
            }), 400

    if 'location' in request.json and type(request.json['location']) is not str:
        return jsonify(
            {
                'status': 400,
                'error': 'location should be a string'
            }), 400

    redflag[0]['location'] = request.json.get('location', redflag[0]['location'])
    redflags.append(redflag[0])
    return jsonify({
        'task': redflag[0],
        'status': 210,
        'id': redflag[0]['id'],
        'message': 'Updated red-flag record\'s location'}), 210


@app.route('/api/v1/PUT/redflags/<int:redflag_id>/edit_comment', methods=['PUT'])
def update_comment(redflag_id):
    redflag = [redflag for redflag in redflags if redflag['id'] == redflag_id]
    if len(redflag) == 0:
        return jsonify({'status': 404,
                        'error': 'No redflag available'}), 404

    if not request.json:
        return jsonify(
            {
                'status': 400,
                'error': 'Use the required format'
            }), 400

    if 'comment' in request.json and type(request.json['comment']) is not str:
        return jsonify(
            {
                'status': 400,
                'error': 'location should be a string'
            }), 400

    redflag[0]['comment'] = request.json.get('comment', redflag[0]['comment'])
    redflags.append(redflag[0])
    data1 = [{'redflag': redflag[0], 'message': 'Updated red-flag record\'s comment'}]
    return jsonify({
        'data': data1,
        'status': 210,
    }), 210


@app.route('/api/v1/DELETE/redflags/<int:redflag_id>', methods=['DELETE'])
def delete_redflag(redflag_id):
    redflag = [redflag for redflag in redflags if redflag['id'] == redflag_id]
    if len(redflag) == 0:
        return jsonify(
            {
                'status': 404,
                'error': 'Redflag with that ID is not available'
            }), 404
    redflags.remove(redflag[0])
    redfla = [{'message': 'red-flag record has been deleted',
               'id': redflag[0]['id'], 'redflag': redflag[0]}]
    return jsonify({
        'status': 206,
        'data': redfla,

    }), 206


if __name__ == '__main__':
    app.run(debug=True)
