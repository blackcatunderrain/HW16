from models import *


def get_all(model) -> list[dict]:
    result = []
    for raw in db.session.query(model).all():
        result.append(raw.to_dict())
    return result


def get_all_by_id(model, find_id):
    try:
        return db.session.query(model).get(find_id).to_dict()
    except Exception:
        return {}
