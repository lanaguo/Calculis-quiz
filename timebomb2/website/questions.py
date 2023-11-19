from flask import Blueprint, render_template, request, flash, redirect, url_for

questions = Blueprint('questions', __name__)

# defining all rqs that this root can get (by default, only get)
@questions.route('/derivatives')
def derivatives():
    return render_template("derivatives.html")

@questions.route('/integrals')
def integrals():
    return render_template("integrals.html")
