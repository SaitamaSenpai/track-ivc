from flask import Blueprint, render_template, redirect, request, flash, url_for
from flask_login import (
	    login_user,
	    current_user)
from track.blueprints.user.decorators import anonymous_required

page = Blueprint('page', __name__, template_folder='templates')


@page.route('/')
@anonymous_required()
def home():
	from lib.safe_next_url import safe_next_url
	from track.blueprints.user.models import User
	from track.blueprints.user.forms import LoginForm
	form = LoginForm(next=request.args.get('next'))
	if form.validate_on_submit():
		u = User.find_by_identity(request.form.get('identity'))
		if u and u.authenticated(password=request.form.get('password')):
			# As you can see remember me is always enabled, this was a design
            # decision I made because more often than not users want this
            # enabled. This allows for a less complicated login form.
            #
            # If however you want them to be able to select whether or not they
            # should remain logged in then perform the following 3 steps:
            # 1) Replace 'True' below with: request.form.get('remember', False)
            # 2) Uncomment the 'remember' field in user/forms.py#LoginForm
            # 3) Add a checkbox to the login form with the id/name 'remember'
			if login_user(u, remember=request.form.get('remember', False)) and u.is_active():
				u.update_activity_tracking(request.remote_addr)

				# Handle optionally redirecting to the next URL safely.
				next_url = request.form.get('next')
				if next_url:
					return redirect(safe_next_url(next_url))
				return redirect(url_for('user.view'))
			else:
				flash('This account has been disabled.', 'error')
		else:
			flash('Identity or password is incorrect.', 'error')

	return render_template('user/login.html', form=form)


@page.route('/terms')
def terms():
    return render_template('page/terms.html')


@page.route('/privacy')
def privacy():
    return render_template('page/privacy.html')

@page.route('/about')
def about():
	return render_template('page/about.html')
