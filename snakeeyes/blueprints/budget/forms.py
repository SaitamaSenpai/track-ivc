from flask_wtf import Form
from wtforms import StringField, IntegerField, FloatField, SelectField, TextAreaField
from wtforms.validators import DataRequired, Length, Optional, Regexp, NumberRange
from wtforms_components import Unique
from lib.util_wtforms import choices_from_dict

from snakeeyes.blueprints.budget.models import Budget, db
'''
class SearchForm(Form):
    q = StringField('Search terms', [Optional(), Length(1, 256)])
'''

class BudgetForm(Form):
	budget_year = StringField('Budget Year', [DataRequired()])
	description = TextAreaField('Description', [DataRequired(), Length(1, 8192)])
	input_type_balance = FloatField('Amount ($)', [DataRequired(), NumberRange(min=0.00, max=21474836.47)])

	ledger_acct_code = SelectField('Code', [DataRequired()], 
											choices=choices_from_dict(Budget.ledger_acct_code, 
																	  prepend_blank=False))

	program_name = SelectField('Program Name', [DataRequired()],
												choices=choices_from_dict(Budget.program_names,
																		  prepend_blank=False))

	input_type = SelectField('Type', [DataRequired()],
									  choices=choices_from_dict(Budget.input_type,
									  							prepend_blank=False))
