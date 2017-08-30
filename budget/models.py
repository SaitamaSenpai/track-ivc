from collections import OrderedDict

from track.extensions import db
from lib.util_sqlalchemy import ResourceMixin

class Budget(ResourceMixin, db.Model):

	INPUT_TYPE = OrderedDict([
        ('allocated', 'Allocated'),
        ('expenses', 'Expenses'),
        ('income', 'Income')
    ])

	ACCT_NUM = OrderedDict([
		('2000 - Salaries/Benefits', '2000 - Salaries/Benefits'),
		('3000 - Benefits', '3000 - Benefits'),
		('4000 - Books and Supplies', '4000 - Books and Supplies'),
		('5000 - Other Operating Expenses', '5000 - Other Operating Expenses'),
		('6000 - Capital Outlay', '6000 - Capital Outlay'),
		('7000 - Other Outgoing', '7000 - Other Outgoing')
	])

	BUD_YR = OrderedDict([
        ('2016-2017', '2016-2017'),
		('2017-2018', '2017-2018'),
        ('2018-2019', '2018-2019'),
		('2019-2020', '2019-2020'),
        ('2020-2021', '2020-2021'),
		('2021-2022', '2021-2022')
    ])

	#table name
	__tablename__ = 'Budget'

	#unique id for each input of this database
	id = db.Column(db.Integer, primary_key=True)

	#id of the user
	user_id = db.Column(db.String, db.ForeignKey('users.username',
                                                  onupdate='CASCADE',
                                                  ondelete='CASCADE'),
                        index=True, nullable=False)

	# data field
	input_type = db.Column(db.Enum(*INPUT_TYPE, name='input_types', native_enum=False),
							nullable=False)
	acct_num = db.Column(db.Enum(*ACCT_NUM, name='account_numbers', native_enum=False),
							nullable=False)
	budget_year = db.Column(db.String(128))
	allocated_amount = db.Column(db.Float())
	expenses_amount = db.Column(db.Float())
	income_amount = db.Column(db.Float())
	
	description = db.Column(db.Text(), nullable=False)
	

	def __init__(self, **kwargs):
		#initialize the whole database
		super(Budget, self).__init__(**kwargs)
	