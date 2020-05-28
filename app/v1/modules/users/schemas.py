"""
User schemas
------------
"""

from flask_marshmallow import base_fields
from flask_marshmallow.schema import Schema
from marshmallow_sqlalchemy import ModelSchema
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema

from .daos import UserDAO


class UserSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = UserDAO
        exclude = ("password_hash",)

        #include_relationships = True
        load_instance = True
        transient = True

    password = base_fields.Inferred()


#class BaseUserSchema(ModelSchema):
#    """
#    Base user schema exposes only the most general fields.
#    """

#    class Meta:
#        # pylint: disable=missing-docstring
#        model = UserDAO
#        fields = (
#            UserDAO.id.key,
#            UserDAO.username.key,
#            UserDAO.email.key,
#            #User.first_name.key,
#            #User.middle_name.key,
#            #User.last_name.key,
#        )
#        dump_only = (
#            UserDAO.id.key,
#        )


#class DetailedUserSchema(BaseUserSchema):
#    """
#    Detailed user schema exposes all useful fields.
#    """

#    class Meta(BaseUserSchema.Meta):
#        fields = BaseUserSchema.Meta.fields + (
#            UserDAO.email.key,
#            #User.created.key,
#            #User.updated.key,
#            #User.is_active.fget.__name__,
#            #User.is_regular_user.fget.__name__,
#            #User.is_admin.fget.__name__,
#        )


#class UserSignupFormSchema(Schema):

#    recaptcha_server_key = base_fields.String(required=True)
