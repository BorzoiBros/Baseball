from flask_wtf import Form
from wtforms import TextField, PasswordField
from wtforms.validators import DataRequired, EqualTo, Length

# Set your classes here.


class RegisterForm(Form):
    name = TextField(
        'User Name', validators=[DataRequired(), Length(min=6, max=25)]
    )
    email = TextField(
        'Email', validators=[DataRequired(), Length(min=6, max=40)]
    )
    password = PasswordField(
        'Password', validators=[DataRequired(), Length(min=6, max=40)]
    )
    confirm = PasswordField(
        'Password Confirmation', validators=[DataRequired(),
        EqualTo('password', message='Password does not match')]
    )


class LoginForm(Form):
    name = TextField('User Name', [DataRequired()])
    password = PasswordField('Password', [DataRequired()])


class ForgotForm(Form):
    email = TextField(
        'Email', validators=[DataRequired(), Length(min=6, max=40)]
    )

class AddTeamForm(Form):
    team_name = TextField(
        'Team Name', validators=[DataRequired(), Length(min=6, max=25)]
    )
    league = TextField(
        'League', validators=[DataRequired(), Length(min=6, max=40)]
    )
    division = TextField(
        'Devision', validators=[DataRequired(), Length(min=1, max=40)]
    )