from flask import session, request
from flask_babel import gettext
from .extensions import babel

# ✅ دالة موحدة واحترافية
def get_locale():
    # 1. إذا تم تمرير اللغة في الرابط (مثلاً عند أول زيارة)
    if "lang" in request.args:
        lang = request.args.get("lang")
        if lang in ['de', 'en', 'ar']:
            session['lang'] = lang  # خزّنها في الجلسة
            return lang

    # 2. إذا تم اختيار لغة مسبقًا
    if "lang" in session:
        return session['lang']

    # 3. fallback للغة المتصفح
    return request.accept_languages.best_match(['de', 'en', 'ar'])

def init_i18n(app):
    babel.locale_selector_func = get_locale

    @app.context_processor
    def inject_get_locale():
        return dict(get_locale=get_locale)

    @app.context_processor
    def inject_translation():
        return dict(gettext=gettext)
