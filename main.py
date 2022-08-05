import json
from config import app
from db_init import init_db
from models import User, Order, Offer
from service import get_all, get_all_by_id


@app.route('/users/', methods=['GET'])
def get_user():
    return app.response_class(
        response=json.dumps(get_all(User), indent=4),
        status=200,
        mimetype='application/json'
    )


@app.route('/orders/', methods=['GET'])
def get_orders():
    return app.response_class(
        response=json.dumps(get_all(Order), indent=4),
        status=200,
        mimetype='application/json'
    )


@app.route('/offers/', methods=['GET'])
def get_offers():
    return app.response_class(
        response=json.dumps(get_all(Offer), indent=4),
        status=200,
        mimetype='application/json'
    )


@app.route('/users/<int:user_id>', methods=['GET'])
def get_user_by_id(user_id):
    data = get_all_by_id(User, user_id)
    return app.response_class(
        response=json.dumps(data, indent=4),
        status=200,
        mimetype='application/json'
    )


@app.route('/orders/<int:order_id>', methods=['GET'])
def get_orders_by_id(order_id):
    data = get_all_by_id(Order, order_id)
    return app.response_class(
        response=json.dumps(data, indent=4),
        status=200,
        mimetype='application/json'
    )


@app.route('/offers/<int:offer_id>', methods=['GET'])
def get_offers_by_id(offer_id):
    data = get_all_by_id(Offer, offer_id)
    return app.response_class(
        response=json.dumps(data, indent=4),
        status=200,
        mimetype='application/json'
    )


if __name__ == '__main__':
    init_db()
    app.run(host='0.0.0.0', port=8080, debug=True)
