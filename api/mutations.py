from datetime import date
from ariadne import convert_kwargs_to_snake_case
from api import db
from api.models import Ad

@convert_kwargs_to_snake_case
def create_ad_resolver(obj, info, subject, body, email, price=None):
    try:
        ad = Ad(
            subject=subject, body=body, email=email, price=price
        )
        db.session.add(ad)
        db.session.commit()
        payload = {
            "success": True,
            "ad": ad.to_dict()
        }
    except ValueError:
        payload = {
            "success": False,
            "errors": [str(error)]
        }
    return payload

@convert_kwargs_to_snake_case
def delete_ad_resolver(obj, info, id):
    try:
        ad = Ad.query.get(id)
        db.session.delete(ad)
        db.session.commit()
        payload = {"success": True, "ad": ad.to_dict()}
    except AttributeError:
        payload = {
            "success": False,
            "errors": ["Not found"]
        }
    return payload