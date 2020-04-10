from flask import Blueprint,render_template, abort, url_for, flash, request, redirect
from app.main.form import ShortForm
from app.models import url_data
from app import db, app
import os, binascii

main = Blueprint('main',__name__)

@main.route("/",methods=['GET','POST'])
@main.route("/home", methods=['GET','POST'])
def home():
    form = ShortForm()
    if form.validate_on_submit():
        current_url = url_data()
        current_url.id =  binascii.b2a_hex(os.urandom(3)).decode('UTF-8')
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

@main.errorhandler(404)
def error_404(e):
    return render_template('error.html',errorcode="404",error_desc=e)
@main.errorhandler(403)
def error_403(e):
    return render_template('error.html',errorcode="403",error_desc=e)
@main.errorhandler(500)
def error_500(e):
    return render_template('error.html',errorcode="500",error_desc=e)