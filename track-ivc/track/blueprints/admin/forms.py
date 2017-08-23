from collections import OrderedDict

from flask_wtf import Form
from wtforms import SelectField, StringField, BooleanField, PasswordField
from wtforms.validators import DataRequired, Length, Optional, Regexp
from wtforms_components import EmailField, Email, Unique

from lib.util_wtforms import ModelForm, choices_from_dict
from track.blueprints.user.models import db, User


class SearchForm(Form):
    q = StringField('Search terms', [Optional(), Length(1, 256)])


class BulkDeleteForm(Form):
    SCOPE = OrderedDict([
        ('all_selected_items', 'All selected items'),
        ('all_search_results', 'All search results')
    ])

    scope = SelectField('Privileges', [DataRequired()],
                        choices=choices_from_dict(SCOPE, prepend_blank=False))


class UserForm(ModelForm):
    username_message = 'Letters, numbers and underscores only please.'

    username = StringField(validators=[
        Unique(
            User.username,
            get_session=lambda: db.session
        ),
        Optional(),
        Length(1, 16),
        Regexp('^\w+$', message=username_message)
    ])

    role = SelectField('Privileges', [DataRequired()],
                       choices=choices_from_dict(User.ROLE,
                                                 prepend_blank=False))
    active = BooleanField('Yes, allow this user to sign in')

    email = EmailField(validators=[
        Optional(),
        Email(),
        Unique(
            User.email,
            get_session=lambda: db.session
        )
    ])
    acct_type = SelectField('Account Type', [DataRequired()], 
                                            choices=choices_from_dict(User.ACCT_TYPE, 
                                                                        prepend_blank=True))
'''
class AddForm(ModelForm):
    username_message = 'Letters, numbers and underscores only please.'

    username = StringField(validators=[
        Unique(
            User.username,
            get_session=lambda: db.session
        ),
        Optional(),
        Length(1, 16),
        Regexp('^\w+$', message=username_message)
    ])

    role = SelectField('Privileges', [DataRequired()],
                       choices=choices_from_dict(User.ROLE,
                                                 prepend_blank=False))
    active = BooleanField('Yes, allow this user to sign in')

    email = EmailField(validators=[
        Optional(),
        Email(),
        Unique(
            User.email,
            get_session=lambda: db.session
        )
    ])
    acct_type = SelectField('Account Type', [DataRequired()], 
                                            choices=choices_from_dict(User.ACCT_TYPE, 
                                                                        prepend_blank=True))
    password = PasswordField('Password', [DataRequired(), Length(8, 128)])
    '''
