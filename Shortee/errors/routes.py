from flask import Blueprint,render_template

error = Blueprint('error',__name__)

@error.errorhandler(404)
def error_404():
    return render_template('error.html',errorcode="404",error_desc="File Not Found!")
@error.errorhandler(403)
def error_403():
    return render_template('error.html',errorcode="403",error_desc="Access forbidden!")
@error.errorhandler(500)
def error_500():
    return render_template('error.html',errorcode="500",error_desc="Unknown Error")