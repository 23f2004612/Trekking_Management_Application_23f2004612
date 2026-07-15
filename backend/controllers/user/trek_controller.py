from flask import jsonify
from decorators.roles import user_required
from models.trek import Trek
from schemas.trek_schema import treks_schema, trek_schema
from services.redis_service import (
    get_cache,
    set_cache
)

def available_treks():

    cache_key = "available_treks"

    cached = None
    try:
        cached = get_cache(cache_key)
    except Exception:
        pass

    if cached is not None:
        return jsonify({
            "success": True,
            "treks": cached
        }), 200

    treks = Trek.query.filter_by(status="Open").all()
    result = treks_schema.dump(treks)

    if result:
        try:
            set_cache(cache_key, result)
        except Exception:
            pass
 
    return jsonify({
        "success": True,
        "treks": result,
        "message": (
            "No treks available at the moment."
            if not result
            else None
        )
    }), 200

def trek_details(trek_id):
    trek = Trek.query.get_or_404(trek_id)
    return trek_schema.dump(trek),200

