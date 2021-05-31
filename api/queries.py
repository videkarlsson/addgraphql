from ariadne import convert_kwargs_to_snake_case
from .models import Ad
from sqlalchemy import asc
from sqlalchemy import desc


def sortByToField(sortBy):
    if sortBy['field'] == "PRICE":
        return Ad.price
    
    if sortBy['field'] == "CREATED_AT":
        return Ad.created_at
    
    raise Exception("Unsupported sort field: " + sortBy['field'] + 
        " allowed values: PRICE, CREATED_AT")

def sortByToOrderFunction(sortBy):

    if sortBy['order'] == "DESC":
        return desc(sortByToField(sortBy))

    if sortBy["order"] == "ASC":
        return asc(sortByToField(sortBy))

    raise Exception("Unsupported order : " + sortBy['order'] + 
        " allowed values: DESC, ASC")


def queryOrderedAds(sortBy):
    if sortBy == None:
        Ad.query.all()

    return Ad.query.order_by(sortByToOrderFunction(sortBy)).all()

def listAds_resolver(obj, info, sortBy):
    try:
        ads = [ad.to_dict() for ad in queryOrderedAds(sortBy)]
        payload = {
            "success": True,
            "ads": ads
        }
    except Exception as error:
        payload = {
            "success": False,
            "errors": [str(error)]
        }
    return payload


@convert_kwargs_to_snake_case
def getAd_resolver(obj, info, id):
    try:
        ad = Ad.query.get(id)
        payload = {
            "success": True,
            "ad": ad.to_dict()
        }
    except AttributeError:  # todo not found
        payload = {
            "success": False,
            "errors": ["Ad matching {id} not found"]
        }
    return payload
