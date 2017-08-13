from flask import (
    Blueprint,
    redirect,
    request,
    flash,
    url_for,
    render_template)

from flask_login import login_required, current_user

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
def input():
    form = BudgetForm()

    budget = Budget()
    create = Budget.add(user=current_user,
                        budget_year=request.form.get('budget_year'),
                        user_id = current_user.id)
    if create:
        flash(_('Your subscription has been updated.'), 'success')
        return redirect(url_for('user.settings'))

    return render_template('budget/input.html', form=form)
