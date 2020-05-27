"""
Input arguments (Parameters) for User resources RESTful API
-----------------------------------------------------------
"""

from flask_marshmallow import base_fields, Schema

from . import schemas
from .models import User


class AddUserParameters(schemas.BaseUserSchema):
    """
    New user creation (sign up) parameters.
    """

    username = base_fields.String(description="Example: root", required=True)
    email = base_fields.Email(description="Example: root@gmail.com", required=True)
    password = base_fields.String(description="No rules yet", required=True)

    class Meta(schemas.BaseUserSchema.Meta):
        fields = schemas.BaseUserSchema.Meta.fields + (
            'email',
            'password',
        )
