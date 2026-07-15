from extensions import ma
from models.booking import Booking
from marshmallow import fields
from schemas.trek_schema import TrekSchema

class BookingSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Booking
        load_instance = True

    trek = fields.Nested(
        TrekSchema,
        only=(
            "id",
            "trek_name",
            "location",
            "difficulty",
            "duration",
            "description",
            "available_slots",
            "booked_slots",
            "status",
            "start_date",
            "end_date",
        ),
    )

booking_schema = BookingSchema()
bookings_schema = BookingSchema(many=True)