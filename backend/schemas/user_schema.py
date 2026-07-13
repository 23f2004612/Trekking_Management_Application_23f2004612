from extensions import ma
from models.user import User

class UserSchema(ma.SQLAlchemySchema):

    class Meta:
        model = User

    id = ma.auto_field()
    full_name = ma.auto_field()
    email = ma.auto_field()
    contact_number = ma.auto_field()
    role = ma.auto_field()
    status = ma.auto_field()

    specialization = ma.auto_field()
    experience = ma.auto_field()

    created_at = ma.auto_field()
    
user_schema = UserSchema()
users_schema = UserSchema(many=True)
