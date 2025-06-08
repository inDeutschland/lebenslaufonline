from flask import Blueprint, request, session, render_template, redirect, url_for
from flask_babel import _
from flask_babel import force_locale
from ..i18n_runtime import get_locale



main_bp = Blueprint("main", __name__)


@main_bp.route("/")
def home():
    lang = get_locale()
    with force_locale(lang):
        print("🌐 Forced locale:", lang)
        return render_template("home.html.j2", test=_("Select language:"))

@main_bp.route('/set_language/<lang>')
def set_language(lang):
    session['lang'] = lang
    return redirect(request.referrer or url_for('main.home'))  # يرجع للصفحة السابقة

