from flask import jsonify
from decorators.roles import user_required
from models.trek import Trek
from schemas.trek_schema import treks_schema, trek_schema
from services.redis_service import (
    get_cache,
    set_cache
)

@user_required
def available_treks():

    cache_key = "available_treks"

    cached = get_cache(cache_key)

    if cached:
        return cached, 200

    treks = Trek.query.filter_by(
        status="Open"
    ).all()

    result = treks_schema.dump(treks)

    set_cache(cache_key, result)

    return result, 200

@user_required
def trek_details(trek_id):
    trek = Trek.query.get_or_404(trek_id)
    return trek_schema.dump(trek),200

