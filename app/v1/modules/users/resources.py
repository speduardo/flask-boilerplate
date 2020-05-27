from flask_restplus import Resource, Namespace, fields
from app.v1.extensions import db
from .models import UserModel
from .dto import User, UserSchema
from .dao import UserDAO

api = Namespace('users', description="Users")


@api.route('/')
class UserList(Resource):
    """
    Manipulations with users.
    """

    #@api.login_required(oauth_scopes=['users:read'])
    #@api.permission_required(permissions.AdminRolePermission())
    #@api.response(200, 'Success', schemas.BaseUserSchema(many=True))
    #@api.paginate()
    @api.marshal_list_with(UserModel.model, envelope='data')
    def get(self):
        """
        List of users.
        Returns a list of users starting from ``offset`` limited by ``limit``
        parameter.
        """
        userList = UserDAO().findAll()
        return userList

    #@api.parameters(user)
    #@api.response(schemas.DetailedUserSchema())
    #@api.response(code=HTTPStatus.FORBIDDEN)
    #@api.response(code=HTTPStatus.CONFLICT)
    @api.doc('create_user')
    @api.expect(UserModel.model)
    @api.marshal_with(UserModel.model, code=201)
    def post(self):
        """
        Create a new user.
        """
        #with api.commit_or_abort(
        #        db.session,
        #        default_error_message="Failed to create a new user."
        #):
        #new_user = User(**args)
        #db.session.add(new_user)
        #userSchema = UserSchema()
        #load_data = userSchema.load(api.payload, session=db.session)
        #db.session.add(load_data)
        data = api.payload
        new_user = UserSchema().load(api.payload)
        db.session.add(new_user)
        db.session.commit()
        db.session.flush()

        return new_user, 201


@api.route('/<int:user_id>')
#@api.login_required(oauth_scopes=['users:read'])
#@api.response(
#    code=HTTPStatus.NOT_FOUND,
#    description="User not found.",
#)
#@api.resolve_object_by_model(User, 'user')
class User(Resource):
    """
    Manipulations with a specific user.
    """

    #@api.permission_required(
    #    permissions.OwnerRolePermission,
    #    kwargs_on_request=lambda kwargs: {'obj': kwargs['user']}
    #)
    #@api.response(200, 'Success', schemas.DetailedUserSchema())
    def get(self, user):
        """
        Get user details by ID.
        """
        return user

    #@api.login_required(oauth_scopes=['users:write'])
    #@api.permission_required(
    #    permissions.OwnerRolePermission,
    #    kwargs_on_request=lambda kwargs: {'obj': kwargs['user']}
    #)
    #@api.permission_required(permissions.WriteAccessPermission())
    #@api.parameters(parameters.PatchUserDetailsParameters())
    #@api.response(200, 'Success', schemas.DetailedUserSchema())
    #@api.response(code=HTTPStatus.CONFLICT)
    def patch(self, args, user):
        """
        Patch user details by ID.
        """
        with api.commit_or_abort(
                db.session,
                default_error_message="Failed to update user details."
        ):
            #parameters.PatchUserDetailsParameters.perform_patch(args, user)
            db.session.merge(user)
        return user


@api.route('/signup-form')
class UserSignupForm(Resource):
    """
    Use signup form helpers.
    """

    #@api.response(200, 'Success', schemas.UserSignupFormSchema())
    def get(self):
        """
        Get signup form keys.
        This endpoint must be used in order to get a server reCAPTCHA public key which
        must be used to receive a reCAPTCHA secret key for POST /users/ form.
        """
        # TODO:
        return {"recaptcha_server_key": "TODO"}


@api.route('/me')
#@api.login_required(oauth_scopes=['users:read'])
class UserMe(Resource):
    """
    Useful reference to the authenticated user itself.
    """

    #@api.response(200, 'Success', schemas.DetailedUserSchema())
    def get(self):
        """
        Get current user details.
        """
        return User.query.get_or_404(current_user.id)
