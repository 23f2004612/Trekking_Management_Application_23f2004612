from extensions import ma
from models.booking import Booking

class BookingSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Booking
        load_instance = True

booking_schema = BookingSchema()
bookings_schema = BookingSchema(many=True)