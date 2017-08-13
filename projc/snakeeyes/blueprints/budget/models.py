from lib.util_sqlalchemy import ResourceMixin
from snakeeyes.extensions import db
from sqlalchemy import or_
from collections import OrderedDict

class Budget(ResourceMixin, db.Model):
	ledger_acct_code = OrderedDict([
		('2000 - Salaries/Benefits', '2000 - Salaries/Benefits'),
		('3000 - Benefits', '3000 - Benefits'),
		('4000 - Books and Supplies', '4000 - Books and Supplies'),
		('5000 - Other Operating Expenses', '5000 - Other Operating Expenses'),
		('6000 - Capital Outlay', '6000 - Capital Outlay'),
		('7000 - Other Outgoing', '7000 - Other Outgoing')
	])

	program_names = OrderedDict([
		('Club', 'club'),
		('Co-Curricular', 'co-curricular'),
		('Department', 'department'),
		('ASG of IVC', 'asg of ivc'),
		('Student Life', 'student life')
	])

	input_type = OrderedDict([
		('Allocated', 'allocated'),
		('Expenses', 'expenses'),
		('Income', 'income')
	])


	__tablename__='budget'

	id = db.Column(db.Integer, primary_key=True)

	# Relationships.
	user_id = db.Column(db.Integer, db.ForeignKey('users.id',
												  onupdate='CASCADE',
												  ondelete='CASCADE'),
						index=True, nullable=False)

	# Budget details.
	budget_year = db.Column(db.String(), nullable=False)
	description = db.Column(db.String())
	input_type_balance = db.Column(db.Integer())


	def __init__(self, **kwargs):
		super(Budget, self).__init__(**kwargs)

		@classmethod
		def search(cls, query):

			"""
        Search a resource by 1 or more fields.

        :param query: Search query
        :type query: str
        :return: SQLAlchemy filter
        """

			if not query:
					return ''

        	search_query = '%{0}%'.format(query)

        	return or_(Coupon.code.ilike(search_query))
