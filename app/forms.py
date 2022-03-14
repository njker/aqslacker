from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class WalletForm(FlaskForm):
    wallet = StringField("Wallet Address", validators=[DataRequired()])
    submit = SubmitField('Query Data')