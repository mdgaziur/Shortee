from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import URL,DataRequired
from validators import url as uchecker
from wtforms import ValidationError

class ShortForm(FlaskForm):
    url = StringField(
        validators=[
            DataRequired(),
            URL(message="Must be a valid url!")
        ]
    )

    submit = SubmitField(
        'Short it!'
    )