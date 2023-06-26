from flask import Blueprint, request, url_for, redirect, render_template, flash
from ..models.links import Link, generate_short_url
from ..extensions import db, login_manager, cache, limiter
from flask_login import login_required, current_user
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import InputRequired, Length, ValidationError
from urllib.parse import urlparse
from datetime import datetime


shorts = Blueprint('shorts', __name__)
login_manager.login_view = "users.login"


class LinkForm(FlaskForm):
    url = StringField('Url', validators=[
                            InputRequired(), Length(min=10, max=100)], render_kw={"placeholder": "URL"})
    custom_url = StringField('Custom_url', validators=[
                            Length(min=5, max=10)], render_kw={"placeholder": "Want to customise your URL? (Optional)"}) 
    submit = SubmitField('Generate Link')

    def validate_url(self, url):
        url = urlparse(url.data)
        if not url.scheme or not url.netloc:
            print('invalid url')
            raise ValidationError('Invalid URL! Please enter valid URL!')



@shorts.route('/')
def index():
    return render_template('index.html', title='Home Page')



@shorts.route('/<short_url>')
def redirect_url(short_url):
    link = Link.query.filter_by(short_url=short_url).first()


    if link:
        link.visits += 1
        db.session.commit()
        return redirect(link.original_url)

    else:
        return
        flash('Invalid URL')
        return redirect(url_for('link'))



@shorts.route('/shorten_link', methods=['GET', 'POST'])
@limiter.limit("10/minute")
@cache.memoize(timeout=30)
@login_required
def link():
    form = LinkForm()
    if request.method == 'POST':
        try:
            if form.validate_on_submit():
                url = form.url.data
                short_url = form.custom_url.data

                if short_url and Link.query.filter_by(short_url=short_url).first() is not None:
                    flash('Please enter different custom url!')
                    return redirect(url_for('shorts.link'))

                if not url:
                    flash('The URL is required!')
                    return redirect(url_for('shorts.link'))

                if not short_url:
                    short_url = generate_short_url(6)

                new_link = Link(
                    original_url=url, short_url=short_url, date_created=datetime.now())
                db.session.add(new_link)
                db.session.commit()
                shortened_url = request.host_url + short_url

                return render_template('link_added.html', original_url=url, shortened_url=shortened_url)
        except Exception as e:
            print(f'Error - {e}')

    return render_template('link.html', form=form)



@shorts.route('/stats')
@cache.cached(timeout=10)
@login_required
def stats():
    links = Link.query.all()

    return render_template('stats.html', links=links)



@shorts.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404