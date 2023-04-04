from .models import User, Note, Expenditure, Enrolment, institutional_distribution
from . import db, ma


class UserSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = User
        load_instance = True
        sqla_session = db.session
        include_relationships = True


class NoteSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Note
        load_instance = True
        sqla_session = db.session
        include_relationships = True
        
    
class ExpenditureSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Expenditure
        load_instance = True
        sqla_session = db.session
        
        
class EnrolmentSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Enrolment
        load_instance = True
        sqla_session = db.session
        
        
class institutional_distributionSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = institutional_distribution
        load_instance = True
        sqla_session = db.session