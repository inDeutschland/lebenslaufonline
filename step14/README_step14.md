# 📄 README – step14: Language Management using `session` in Flask

## 🎯 Goal:
تنفيذ نظام احترافي متعدد اللغات يSupport التبديل بين العربية، الإنجليزية، والألمانية باستخدام `Flask-Babel` و`session`.

---

## ✅ Tasks Implemented:

### 1. 1. Flask-Babel Setup:
- - Activated `Flask-Babel` inside `create_app()`.
- - Default locale set to اللغة الافتراضية: `ar`.
- - Translations directory configured: مسار الترجمة: `step14/translations`.

---

### 2. 2. Custom `get_locale()` Function:
First checks من `request.args['lang']` (لتسجيل الدخول الأول أو المشاركة)، then from `session['lang']`، then fallback to `request.accept_languages`.

```python
def get_locale():
    if "lang" in request.args:
        lang = request.args.get("lang")
        if lang in ['de', 'en', 'ar']:
            session['lang'] = lang
            return lang
    if "lang" in session:
        return session['lang']
    return request.accept_languages.best_match(['de', 'en', 'ar'])
```

---

### 3. 3. Language Switch Route:

```python
@app.route('/set_language/<lang>')
def set_language(lang):
    session['lang'] = lang
    return redirect(request.referrer or url_for('main.home'))
```

---

### 4. 4. Using `force_locale()` with templates in every route يستخدم `render_template()`:

```python
with force_locale(get_locale()):
    return render_template("...")
```

---

### 5. 5. Language Switch HTML (in `navbar.html.j2`:

```html
<span style="float: right;">
    <a href="{{ url_for('main.set_language', lang='ar') }}">🇸🇦</a>
    <a href="{{ url_for('main.set_language', lang='en') }}">🇺🇸</a>
    <a href="{{ url_for('main.set_language', lang='de') }}">🇩🇪</a>
</span>
```

---

### 6. 6. Integration with Jinja Templates:
- استخدام `{{ _('Text') }}` in every النصوص القابلة للترجمة.
- استخدام `{{ get_locale() }}` inside HTML لتعريف اللغة النشطة.

---

## 📌 Technical Notes:
- الجلسة مشفّرة وstored في Cookie.
- لا حاجة لإعادة تمرير اللغة in every رابط.
- التبديل فوري، ويؤثر على كل الصفحات.

---

## 🔮 Possible Future Enhancements:
- Link language to authenticated user (تخزين في قاعدة البيانات).
- Display selected language in generated PDF التوليدي.
- Support Locale-specific formatting (مثل التاريخ والوقت).