from flask_wtf import Form
from wtforms import TextField, PasswordField
from wtforms.validators import DataRequired, EqualTo, Length

# Set your classes here.


class RegisterForm(Form):
    name = TextField(
        'ユーザー名', validators=[DataRequired(), Length(min=6, max=25)]
    )
    email = TextField(
        'Email', validators=[DataRequired(), Length(min=6, max=40)]
    )
    password = PasswordField(
        'パスワード', validators=[DataRequired(), Length(min=6, max=40)]
    )
    confirm = PasswordField(
        'パスワード確認', validators=[DataRequired(),
        EqualTo('password', message='パスワードが一致しません')]
    )


class LoginForm(Form):
    name = TextField('ユーザー名', [DataRequired()])
    password = PasswordField('Password', [DataRequired()])


class ForgotForm(Form):
    email = TextField(
        'Email', validators=[DataRequired(), Length(min=6, max=40)]
    )

class AddTeamForm(Form):
    team_name = TextField(
        'チーム名', validators=[DataRequired(), Length(min=6, max=25)]
    )
    league = TextField(
        'リーグ', validators=[DataRequired(), Length(min=6, max=40)]
    )
    division = TextField(
        'ディビジョン (部)', validators=[DataRequired(), Length(min=1, max=40)]
    )