from flask import (
    Blueprint,
    redirect,
    request,
    flash,
    url_for,
    render_template)

from lib.safe_next_url import safe_next_url
from flask_login import login_required, current_user
from sqlalchemy import text

from snakeeyes.blueprints.budget.models import Budget
from snakeeyes.blueprints.budget.forms import BudgetForm

budget = Blueprint('budget', __name__, template_folder='templates', url_prefix='/budget')


@budget.before_request
@login_required
def before_request():
	pass

'''
@budget.route('/view', methods=['GET', 'POST'])
@budget.route('/view/page/<int:page>')
def view(page):
	search_form = SearchForm()

	sort_by = Budget.sort_by(request.args.get('sort', 'budget_year'),
							 request.args.get('direction', 'desc'))

	order_values = '{0} {1}'.format(sort_by[0], sort_by[1])

        paginated_users = Budget.query \
            .filter(Budget.search(request.args.get('q', ''))) \
            .order_by(Budget.budget_year.asc(), Budget.ledger_acct_code, text(order_values)) \
            .paginate(page, 50, True)

        return render_template('budget/view.html',
                           form=search_form, bulk_form=bulk_form,
                           users=paginated_users)
'''
@budget.route('/input', methods=['GET', 'POST'])
def input(id):
    b = Budget.query.get(id)
    form = BudgetForm(obj=b)

    b.budget_year = request.form.get('Budget Year')
    b.description = request.form.get('Description')
    if validate_on_submit():
        form.populate_obj(b)
        b.save()

    return render_template('budget/input.html', form=form)