from flask import (
    Blueprint,
    redirect,
    request,
    flash,
    url_for,
    render_template)

from flask_login import login_required, current_user
from track.blueprints.user.decorators import role_required
from sqlalchemy import func

from track.blueprints.budget.models import Budget
from track.blueprints.budget.forms import BudgetForm

budget = Blueprint('budget', __name__, template_folder='templates', url_prefix='/budget')


@budget.before_request
@login_required
def before_request():
	pass

@budget.route('/input', methods=['GET', 'POST'])
@role_required('admin', 'bnf')
def input():
    form = BudgetForm()
    from track.blueprints.user.models import User

    if form.validate_on_submit():
        budget_year = request.form.get('budget_year')
        username = request.form.get('username')
        input_type = request.form.get('input_type')
        acct_num = request.form.get('acct_num')
        amount = request.form.get('amount')
        description = request.form.get('description')

        u = User.find_by_identity(username)

        if input_type == 'allocated':
            a = amount,
            e = 0.0,
            i = 0.0
            u.update_allocated_total(amount)
        if input_type == 'expenses':
            e = amount,
            a = 0.0,
            i = 0.0
            u.update_expenses_total(amount)
        if input_type == 'income':
            i = amount,
            a = 0.0,
            e = 0.0
            u.update_income_total(amount)

        params = {
            'user_id': username,
            'budget_year': budget_year,
            'input_type': input_type,
            'acct_num': acct_num,
            'description': description,
            'allocated_amount': a,
            'expenses_amount': e,
            'income_amount': i
        }
    
        b = Budget(**params)

        if None in params:
            flash('Area missing.', 'error')
        else:    
            b.save()
            flash('Your budget has been saved.', 'success')
            return redirect(url_for('admin.users'))
    

    return render_template('budget/input.html', form=form)

@budget.route('/view', defaults={'page': 1})
@budget.route('/view/page/<int:page>')
@role_required('admin', 'bnf')
def view(page):
    from track.blueprints.user.models import User, db
    from track.blueprints.admin.models import Dashboard
    user = User.query.filter(User.username == Dashboard.hold)
    paginated_budget = Budget.query \
        .filter(Budget.user_id == Dashboard.hold) \
        .order_by(Budget.acct_num.asc(), Budget.updated_on.asc()) \
        .paginate(page, 50, True)

    return render_template('budget/view.html', budget=paginated_budget, user=user)
