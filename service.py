from models import *


def get_all_users():
    result = []
    for raw in User.query.all():
        result.append(raw.to_dict())
    return result
