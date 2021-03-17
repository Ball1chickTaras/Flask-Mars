from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField, BooleanField
from wtforms.validators import DataRequired


class AddJobForm(FlaskForm):
    job = StringField('Job title', validators=[DataRequired()])
    team_leader = IntegerField('Team leader id', validators=[DataRequired()])
    work_size = IntegerField('Work size', validators=[DataRequired()])
    collaborators = StringField('Collaborators', validators=[DataRequired()])
    is_finished = BooleanField('Is job finished')
    submit = SubmitField('Войти')
