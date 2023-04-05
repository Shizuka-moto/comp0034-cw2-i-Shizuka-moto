from .models import User, Note, Expenditure, Enrolment, institutional_distribution
from . import db, ma


class UserSchema(ma.SQLAlchemyAutoSchema):
    """User schema class based on User model."""

    class Meta:
        model = User
        load_instance = True
        sqla_session = db.session
        include_relationships = True


class NoteSchema(ma.SQLAlchemyAutoSchema):
    """Note schema class based on Note model."""

    class Meta:
        model = Note
        load_instance = True
        sqla_session = db.session
        include_relationships = True


class ExpenditureSchema(ma.SQLAlchemyAutoSchema):
    """Expenditure schema class based on Expenditure model."""

    class Meta:
        model = Expenditure
        load_instance = True
        sqla_session = db.session


class EnrolmentSchema(ma.SQLAlchemyAutoSchema):
    """Enrolment schema class based on Enrolment model."""

    class Meta:
        model = Enrolment
        load_instance = True
        sqla_session = db.session


class institutional_distributionSchema(ma.SQLAlchemyAutoSchema):
    """Institutional distribution schema class based on institutional_distribution model."""

    class Meta:
        model = institutional_distribution
        load_instance = True
        sqla_session = db.session
