from wtforms.validators import ValidationError


def ensure_identity_exists(form, field):
    """
    Ensure an identity exists.

    :param form: wtforms Instance
    :param field: Field being passed in
    :return: None
    """
    from track.blueprints.user.models import User
    user = User.find_by_identity(field.data)

    if not user:
        raise ValidationError('Unable to locate account.')


def ensure_existing_password_matches(form, field):
    """
    Ensure that the current password matches their existing password.

    :param form: wtforms Instance
    :param field: Field being passed in
    :return: None
    """
    from track.blueprints.user.models import User
    user = User.query.get(form._obj.id)

    if not user.authenticated(password=field.data):
        raise ValidationError('Does not match.')

def ensure_float(form, field):
    temp = field.data - round(field.data, 2)
    if temp != 0:
        raise ValidationError('Please enter a valid amount (2 decimals).')
