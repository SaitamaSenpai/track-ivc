from snakeeyes.extensions import db
from lib.util_sqlalchemy import ResourceMixin

class Budget(ResourceMixin, db.Model):
	__tablename__ = 'Budget'
	id = db.Column(db.Integer, primary_key=True)

	user_id = db.Column(db.Integer, db.ForeignKey('users.id',
                                                  onupdate='CASCADE',
                                                  ondelete='CASCADE'),
                        index=True, nullable=False)

	budget_year = db.Column(db.String(128))

	def __init__(self, budget_year, user_id):
		self.budget_year = budget_year
		self.user_id = user_id
	