# 📄 README – step14: Language Management using `session` in Flask

## 🎯 الهدف:
تنفيذ نظام احترافي متعدد اللغات يدعم التبديل بين العربية، الإنجليزية، والألمانية باستخدام `Flask-Babel` و`session`.

---

## ✅ المهام المنفذة:

### 1. إعداد Flask-Babel:
- تم تفعيل `Flask-Babel` داخل `create_app()`.
- تم تعيين اللغة الافتراضية: `ar`.
- تم تعريف مسار الترجمة: `step14/translations`.

---

### 2. دالة `get_locale()` مخصصة:
يتم أولًا التحقق من `request.args['lang']` (لتسجيل الدخول الأول أو المشاركة)، ثم من `session['lang']`، ثم Fallback إلى `request.accept_languages`.

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

### 3. مسار تغيير اللغة:

```python
@app.route('/set_language/<lang>')
def set_language(lang):
    session['lang'] = lang
    return redirect(request.referrer or url_for('main.home'))
```

---

### 4. استخدام `force_locale()` في كل route يستخدم `render_template()`:

```python
with force_locale(get_locale()):
    return render_template("...")
```

---

### 5. شيفرة تغيير اللغة في `navbar.html.j2`:

```html
<span style="float: right;">
    <a href="{{ url_for('main.set_language', lang='ar') }}">🇸🇦</a>
    <a href="{{ url_for('main.set_language', lang='en') }}">🇺🇸</a>
    <a href="{{ url_for('main.set_language', lang='de') }}">🇩🇪</a>
</span>
```

---

### 6. الربط مع Jinja وقوالب `.j2`:
- استخدام `{{ _('Text') }}` في كل النصوص القابلة للترجمة.
- استخدام `{{ get_locale() }}` داخل HTML لتعريف اللغة النشطة.

---

## 📌 ملاحظات تقنية:
- الجلسة مشفّرة وتُخزّن في Cookie.
- لا حاجة لإعادة تمرير اللغة في كل رابط.
- التبديل فوري، ويؤثر على كل الصفحات.

---

## 🔮 خطوات مستقبلية ممكنة:
- ربط اللغة بالمستخدم المسجّل (تخزين في قاعدة البيانات).
- عرض اللغة المختارة في ملف PDF التوليدي.
- دعم Locale-specific formatting (مثل التاريخ والوقت).