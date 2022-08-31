from flask_wtf import FlaskForm
from wtforms import StringField, TimeField,SelectField, SubmitField
from wtforms.validators import DataRequired


class CafeForm(FlaskForm):
    cafe = StringField('Cafe name', validators=[DataRequired()])
    location = StringField(label='Cafe Location o Google Maps', validators=[DataRequired()])
    open = TimeField(label='Opening Time', validators=[DataRequired()])
    closing = TimeField(label='Closing Time', validators=[DataRequired()])
    coffee = SelectField(label='Coffee Rating', choices=['☕', '☕☕', '☕☕☕','☕☕☕☕', '☕☕☕☕☕'], validators=[DataRequired()])
    wifi = SelectField(label='Wifi Strongest Rating', choices=['💪', '💪💪','💪💪💪','💪💪💪💪','💪💪💪💪💪'], validators=[DataRequired()])
    power_socket = SelectField(label='Power Socket Availability', choices=['🔌','🔌🔌','🔌🔌🔌','🔌🔌🔌🔌','🔌🔌🔌🔌🔌'], validators=[DataRequired()])
    submit = SubmitField('Submit')

