from flask import Blueprint, render_template, request, redirect, url_for
from ..models.models import db, Section, Setting  
from flask_babel import force_locale
from ..i18n_runtime import get_locale


admin_bp = Blueprint("admin", __name__, url_prefix="/admin")

@admin_bp.route("/sections", methods=["GET", "POST"])
def manage_sections():
    if request.method == "POST":
        for section_id, content in request.form.items():
            section = Section.query.get(int(section_id))
            if section:
                section.content = content
        db.session.commit()
        return redirect(url_for("admin.manage_sections"))

    sections = Section.query.all()
    return render_template("admin/sections.html.j2", sections=sections)



import json

@admin_bp.route("/settings", methods=["GET", "POST"])
def manage_settings():
    error = None

    settings = Setting.query.all()  # نحتاجها لاحقًا داخل POST

    if request.method == "POST":
        try:
            # إعداد خاص لـ section_title_css من الحقول المرئية
            font_size = request.form.get("section_title_css_font_size")
            color = request.form.get("section_title_css_color")
            weight = request.form.get("section_title_css_weight")

            css_json = {
                "font-size": font_size,
                "color": color,
                "font-weight": weight
            }

            setting = Setting.query.filter_by(key="section_title_css").first()
            if setting:
                setting.value = json.dumps(css_json)

            # إعداد خاص لـ paragraph_css
            p_font_size = request.form.get("paragraph_css_font_size")
            p_color = request.form.get("paragraph_css_color")

            paragraph_css_json = {
                "font-size": p_font_size,
                "color": p_color
            }

            p_setting = Setting.query.filter_by(key="paragraph_css").first()
            if p_setting:
                p_setting.value = json.dumps(paragraph_css_json)

            # إعداد خاص لـ body_font
            body_font = request.form.get("body_font")
            b_setting = Setting.query.filter_by(key="body_font").first()
            if b_setting:
                b_setting.value = body_font

            # تجاهل الحقول المعالجة يدويًا
            skip_keys = [
                "section_title_css_font_size", "section_title_css_color", "section_title_css_weight",
                "paragraph_css_font_size", "paragraph_css_color",
                "body_font"
            ]

            for key, value in request.form.items():
                if key in skip_keys:
                    continue
                s = Setting.query.filter_by(key=key).first()
                if s:
                    json.loads(value.replace("'", '"'))
                    s.value = value

            db.session.commit()
            action = request.form.get("action")
            if action == "save_and_preview":
                return redirect(url_for("public.resume"))
            return redirect(url_for("admin.manage_settings"))


        except Exception as e:
            error = f"❌ Fehler im JSON-Format: {str(e)}"

    # إعدادات للعرض (GET)
    section_title_css_data = {
        "font-size": "20px",
        "color": "#000000",
        "font-weight": "normal"
    }

    paragraph_css_data = {
        "font-size": "14px",
        "color": "#444444"
    }

    body_font_value = "Arial, sans-serif"

    for s in settings:
        if s.key == "section_title_css":
            try:
                section_title_css_data = json.loads(s.value.replace("'", '"'))
            except:
                pass
        elif s.key == "paragraph_css":
            try:
                paragraph_css_data = json.loads(s.value.replace("'", '"'))
            except:
                pass
        elif s.key == "body_font":
            body_font_value = s.value

    with force_locale(get_locale()):
        return render_template(
            "admin/settings.html.j2",
            settings=settings,
            error=error,
            section_title_css_data=section_title_css_data,
            paragraph_css_data=paragraph_css_data,
            body_font_value=body_font_value
        )
