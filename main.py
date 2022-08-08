import json
from flask import request
from config import app
from db_init import init_db, insert_data_user, insert_data_order, insert_data_offer
from models import User, Order, Offer
from service import get_all, get_all_by_id, update_all, delete_all


@app.route('/users/', methods=['GET', 'POST'])
def get_user():
    if request.method == 'GET':
        return app.response_class(
            response=json.dumps(get_all(User), indent=4),
            status=200,
            mimetype='application/json'
        )
    elif request.method == 'POST':
        if isinstance(request.json, list):
            insert_data_user(request.json)
        elif isinstance(request.json, dict):
            insert_data_user([request.json])
        else:
            print("Invalid request method")
    return app.response_class(
        response=json.dumps(request.json, indent=4),
        status=200,
        mimetype='application/json'
    )


@app.route('/orders/', methods=['GET', 'POST'])
def get_orders():
    if request.method == 'GET':
        return app.response_class(
            response=json.dumps(get_all(Order), indent=4),
            status=200,
            mimetype='application/json'
        )
    elif request.method == 'POST':
        if isinstance(request.json, list):
            insert_data_order(request.json)
        elif isinstance(request.json, dict):
            insert_data_order([request.json])
        else:
            print("Invalid request method")
    return app.response_class(
        response=json.dumps(request.json, indent=4),
        status=200,
        mimetype='application/json'
    )


@app.route('/offers/', methods=['GET', 'POST'])
def get_offers():
    if request.method == 'GET':
        return app.response_class(
            response=json.dumps(get_all(Offer), indent=4),
            status=200,
            mimetype='application/json'
        )
    elif request.method == 'POST':
        if isinstance(request.json, list):
            insert_data_offer(request.json)
        elif isinstance(request.json, dict):
            insert_data_offer([request.json])
        else:
            print("Invalid request method")
    return app.response_class(
        response=json.dumps(request.json, indent=4),
        status=200,
        mimetype='application/json'
    )


@app.route('/users/<int:user_id>', methods=['GET', 'PUT', 'DELETE'])
def get_user_by_id(user_id):
    if request.method == 'GET':
        data = get_all_by_id(User, user_id)
        return app.response_class(
            response=json.dumps(data, indent=4),
            status=200,
            mimetype='application/json'
        )
    elif request.method == 'PUT':
        update_all(User, user_id, request.json)
        return app.response_class(
            response=json.dumps(['OK'], indent=4),
            status=200,
            mimetype='application/json'
        )
    elif request.method == 'DELETE':
        delete_all(User, user_id, request.json)
        return app.response_class(
            response=json.dumps(['OK'], indent=4),
            status=200,
            mimetype='application/json'
        )


@app.route('/orders/<int:user_id>', methods=['GET', 'PUT', 'DELETE'])
def get_orders_by_id(user_id):
    if request.method == 'GET':
        data = get_all_by_id(Order, user_id)
        return app.response_class(
            response=json.dumps(data, indent=4),
            status=200,
            mimetype='application/json'
        )
    elif request.method == 'PUT':
        update_all(Order, user_id, request.json)
        return app.response_class(
            response=json.dumps(['OK'], indent=4),
            status=200,
            mimetype='application/json'
        )
    elif request.method == 'DELETE':
        delete_all(Order, user_id, request.json)
        return app.response_class(
            response=json.dumps(['OK'], indent=4),
            status=200,
            mimetype='application/json'
        )


@app.route('/offers/<int:user_id>', methods=['GET', 'PUT', 'DELETE'])
def get_offers_by_id(user_id):
    if request.method == 'GET':
        data = get_all_by_id(Offer, user_id)
        return app.response_class(
            response=json.dumps(data, indent=4),
            status=200,
            mimetype='application/json'
        )
    elif request.method == 'PUT':
        update_all(Offer, user_id, request.json)
        return app.response_class(
            response=json.dumps(['OK'], indent=4),
            status=200,
            mimetype='application/json'
        )
    elif request.method == 'DELETE':
        delete_all(Offer, user_id, request.json)
        return app.response_class(
            response=json.dumps(['OK'], indent=4),
            status=200,
            mimetype='application/json'
        )


if __name__ == '__main__':
    init_db()
    app.run(host='0.0.0.0', port=8080, debug=True)
