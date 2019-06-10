#----------------------------------------------------------------------------#
# Imports
#----------------------------------------------------------------------------#

from flask import Flask, render_template, request, flash, url_for, session, redirect
# from flask.ext.sqlalchemy import SQLAlchemy
from flask_sqlalchemy import SQLAlchemy
import logging
from logging import Formatter, FileHandler
from forms import RegisterForm, LoginForm, ForgotForm, AddTeamForm
import os
from functools import wraps

#----------------------------------------------------------------------------#
# App Config.
#----------------------------------------------------------------------------#

app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app)

from models import User, Team
# Automatically tear down SQLAlchemy.
'''
@app.teardown_request
def shutdown_session(exception=None):
    db_session.remove()

'''
'''

# Login required decorator.
'''
def login_required(test):
    @wraps(test)
    def wrap(*args, **kwargs):
        if 'logged_in' in session:
            return test(*args, **kwargs)
        else:
            flash("Login Required")
            return redirect(url_for('login'))
    return wrap

#----------------------------------------------------------------------------#
# Controllers.
#----------------------------------------------------------------------------#


@app.route('/')
def home():
    return render_template('pages/placeholder.home.html')


@app.route('/about')
def about():
    return render_template('pages/placeholder.about.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    form = LoginForm(request.form)
    if request.method == 'POST':
        user = User.query.filter_by(name=request.form['name']).first()
        if user is not None and user.password == request.form['password']:
            session['logged_in'] = True
            flash('Welcome！')
            return redirect(url_for('demo'))
        else:
            error = 'User name or password is invalid'
            flash(error)
    else:
        error = 'Both fields must be entered'
        flash(error)
    return render_template('forms/login.html', form=form, error=error)


@app.route('/register', methods=['GET', 'POST'])
def register():
    error = None
    form = RegisterForm(request.form)
    if request.method == 'POST' :
        if form.validate_on_submit():
            new_user = User(
                form.name.data,
                form.email.data,
                form.password.data
                )
            db.session.add(new_user)
            db.session.commit()
            flash('Thanks for registration! Please login!')
            return redirect(url_for('login'))
        else:
            flash('The value is incorrect')
    return render_template('forms/register.html', form=form, error=error)


@app.route('/forgot')
def forgot():
    form = ForgotForm(request.form)
    return render_template('forms/forgot.html', form=form)

@app.route('/demo')
@login_required
def demo():
    return render_template('pages/demo.html')

@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    flash('Logged out！')
    return redirect(url_for('login'))

# Error handlers.


@app.errorhandler(500)
def internal_error(error):
    #db_session.rollback()
    return render_template('errors/500.html'), 500


@app.errorhandler(404)
def not_found_error(error):
    return render_template('errors/404.html'), 404

if not app.debug:
    file_handler = FileHandler('error.log')
    file_handler.setFormatter(
        Formatter('%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]')
    )
    app.logger.setLevel(logging.INFO)
    file_handler.setLevel(logging.INFO)
    app.logger.addHandler(file_handler)
    app.logger.info('errors')

@app.route('/add_teams', methods=['GET', 'POST'])
def add_team():
    error = None
    form = AddTeamForm(request.form)
    if request.method == 'POST' :
        if form.validate_on_submit():
            new_team = Team(
                form.team_name.data,
                form.league.data,
                form.division.data
                )
            db.session.add(new_team)
            db.session.commit()
            flash('Thanks for adding team!')
            teams = db.session.query(Team)
            return render_template(
                'forms/add_team.html',
                form=AddTeamForm(request.form),
                teams=teams
                )
            # return redirect(url_for('teams'))
        else:
            flash('The value is incorrect')
    return render_template('forms/add_team.html', form=form, error=error)

@app.route('/delete/<int:team_id>')
@login_required
def delete_team(team_id):
    new_id = team_id
    db.session.query(Team).filter_by(id=new_id).delete()
    db.session.commit()
    flash('Team is deleted successfully')
    return redirect(url_for('add_team'))

#----------------------------------------------------------------------------#
# Launch.
#----------------------------------------------------------------------------#

# Default port:
'''
if __name__ == '__main__':
    app.run()
'''
# Or specify port manually:
# -- '''
# -- if __name__ == '__main__':
# --     port = int(os.environ.get('PORT', 5000))
# --     app.run(host='0.0.0.0', port=port)
# -- '''
