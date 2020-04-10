from flask import Blueprint,render_template, url_for, flash, request, redirect
from Shortee.main.form import ShortForm
from Shortee.models import url_data
from Shortee import db, app
import secrets

main = Blueprint('main',__name__)

@main.route("/",methods=['GET','POST'])
@main.route("/home", methods=['GET','POST'])
def home():
    form = ShortForm()
    if form.validate_on_submit():
        current_url = url_data()
        current_url.id = str(secrets.token_hex(4))
        current_url.url = form.url.data
        db.session.add(current_url)
        db.session.commit()
        flash(f'URL shorted successfully! Shorted Url: ',f'{ "http://"+request.host + "/" +current_url.id}')
    return render_template("home.html",form=form)
@main.route("/about")
def about():
    return render_template("about.html")
@main.route("/<string:shorted>")
def browse_shorted(shorted):
    url_model = url_data.query.filter_by(id=shorted).first_or_404()
    return redirect(url_model.url)