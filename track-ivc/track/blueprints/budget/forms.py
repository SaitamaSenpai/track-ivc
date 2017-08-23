from flask_wtf import Form
from wtforms import StringField, IntegerField, FloatField, SelectField, TextAreaField
from wtforms.validators import DataRequired, Length, Optional, Regexp, NumberRange
from wtforms_components import Unique
from lib.util_wtforms import ModelForm, choices_from_dict

from track.blueprints.budget.models import Budget, db
from track.blueprints.user.validations import ensure_identity_exists, ensure_float

'''
class ViewForm(Form):
	from snakeeyes.blueprints.user.models import User
	acct_type = SelectField('Account Type', [DataRequired()], 
                                            choices=choices_from_dict(User.ACCT_TYPE, 
                                                                        prepend_blank=True))
'''


class BudgetForm(ModelForm):
	username = StringField('Account ID', [DataRequired(),
                            ensure_identity_exists])
	input_type = SelectField('Input Type', [DataRequired()], 
											choices=choices_from_dict(Budget.INPUT_TYPE, prepend_blank=True))
	acct_num = SelectField('Account Number', [DataRequired()], 
											choices=choices_from_dict(Budget.ACCT_NUM, prepend_blank=True))
	budget_year = StringField('Budget Year', [DataRequired()])
	amount = FloatField('Amount ($)', [DataRequired(), NumberRange(min=0.00, max=21474836.47), ensure_float])
	description = TextAreaField('Description', [DataRequired(), Length(1, 8192)])
	