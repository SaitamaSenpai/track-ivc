from snakeeyes.extensions import db

class Budget(db.Model):
	__tablename__ = 'Budget'
	id = db.Column(db.Integer, primary_key=True)
	user_id = db.Column(db.Integer, db.ForeignKey('users.id',
                                                  onupdate='CASCADE',
                                                  ondelete='CASCADE'),
                        index=True, nullable=False)
	budget_year = db.Column(db.String(128))

	def __init__(self, budget_year):
		self.budget_year = budget_year
		self.user_id = user_id
