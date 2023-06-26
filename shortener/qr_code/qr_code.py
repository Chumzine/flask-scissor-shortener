import segno
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import InputRequired, Length, ValidationError
from flask import Blueprint, flash, render_template, request
from flask_login import login_required
from ..extensions import limiter


qrcode = Blueprint('qrcode', __name__)



class QRCodeForm(FlaskForm):
    url = StringField('URL', validators=[
                            InputRequired(), Length(min=10, max=30)],render_kw={"placeholder": "URL"} )
    submit = SubmitField('Generate QR Code')


@qrcode.route('/generate_qr_code', methods=['GET', 'POST'])
@limiter.limit("10/minute")
@login_required
def generate_qr_code():
    form = QRCodeForm()

    if request.method == "POST":
        if form.validate_on_submit():
            url = form.url.data
            qr = segno.make(url)
            qr.save('shortener/static/images/qrcode.png', scale=10)
            flash('QR Code generated')

        return render_template('display_qr_code.html')
    else:
        return render_template('qr_code.html', form=form)