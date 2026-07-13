from marshmallow import fields
from extensions import ma
from models.trek import Trek
from schemas.user_schema import UserSchema

class TrekSchema(ma.SQLAlchemySchema):
    class Meta:
        model = Trek

    id = ma.auto_field()
    trek_name = ma.auto_field()
    location = ma.auto_field()
    difficulty = ma.auto_field()
    duration = ma.auto_field()
    description = ma.auto_field()
    available_slots = ma.auto_field()
    booked_slots = ma.auto_field()
    start_date = ma.auto_field()
    end_date = ma.auto_field()
    status = ma.auto_field()

    assigned_staff = fields.Nested(
        UserSchema,
        only=("id", "full_name")
    )
    
trek_schema = TrekSchema()
treks_schema = TrekSchema(many=True)
