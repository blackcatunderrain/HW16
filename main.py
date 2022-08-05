import json
from config import app
from db_init import init_db
from service import get_all_users


@app.route('/users/', methods=['GET'])
def get_user():
    get_all_users()
    return app.response_class(
        response=json.dumps(get_all_users(), indent=4),
        status=200,
        mimetype='application/json'
    )


@app.route('/users/<int:user_id>', methods=['GET'])
def get_user_by_id(user_id):
    data = get_all_users()
    for raw in data:
        if raw.get('id') == user_id:
            return app.response_class(
                response=json.dumps(raw, indent=4),
                status=200,
                mimetype='application/json'
            )
    return app.response_class(
        response=json.dumps({}, indent=4),
        status=200,
        mimetype='application/json'
    )


if __name__ == '__main__':
    init_db()
    app.run(host='0.0.0.0', port=8080, debug=True)
