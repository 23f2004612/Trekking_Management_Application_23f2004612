from flask import request
from sqlalchemy import or_
from decorators.roles import user_required
from models.trek import Trek
from schemas.trek_schema import treks_schema

def search_treks():

    q = request.args.get("query", "").strip()

    treks = Trek.query.filter(

        Trek.status == "Open",
        or_(
            Trek.trek_name.ilike(f"%{q}%"),
            Trek.location.ilike(f"%{q}%"),
            Trek.difficulty.ilike(f"%{q}%")
        )
    ).all()

    return treks_schema.dump(treks),200
