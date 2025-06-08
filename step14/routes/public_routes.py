from flask import Blueprint, render_template
from ..models.models import Section
from ..logic.builder import get_css_setting

public_bp = Blueprint("public", __name__)

@public_bp.route("/resume")
def resume():
    sections = Section.query.all()
    section_title_css = get_css_setting("section_title_css", "font-size: 20px; color: #000")
    paragraph_css = get_css_setting("paragraph_css", "font-size: 14px; color: #444")
    body_font = get_css_setting("body_font", "font-family: Arial, sans-serif")

    return render_template(
        "public/resume.html.j2",
        sections=sections,
        section_title_css=section_title_css,
        paragraph_css=paragraph_css,
        body_font=body_font
    )
