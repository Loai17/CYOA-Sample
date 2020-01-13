from flask import *
from flask import session as login_session
from sqlalchemy.exc import IntegrityError
# from flask import Flask, request, redirect, url_for, send_from_directory, render_template
from werkzeug.utils import secure_filename
import locale, os


app = Flask(__name__)
app.secret_key = "MY_SUPER_SECRET_KEY"


@app.route('/', methods=['GET'])
def home():
	return render_template('main.html')



if __name__ == '__main__':
    app.run(debug=True)
