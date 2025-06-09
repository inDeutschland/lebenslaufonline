from ..extensions import db


# ✅ الجداول الأصلية (لا تلمس)
class Section(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    order = db.Column(db.Integer, nullable=False)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text, nullable=True)


class Setting(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    key = db.Column(db.String(100), unique=True, nullable=False)
    value = db.Column(db.Text, nullable=False)


# ✅ الجداول الجديدة
class ResumeSection(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    order = db.Column(db.Integer, nullable=False)
    lang = db.Column(db.String(10), nullable=False, default='en')
    is_visible = db.Column(db.Boolean, default=True)

    paragraphs = db.relationship("ResumeParagraph", backref="resume_section", cascade="all, delete-orphan", lazy=True)


class ResumeParagraph(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    resume_section_id = db.Column(db.Integer, db.ForeignKey('resume_section.id'), nullable=False)
    type = db.Column(db.String(50), nullable=False)  # basic, with_description, with_date, etc
    order = db.Column(db.Integer, nullable=False)
    is_visible = db.Column(db.Boolean, default=True)

    fields = db.relationship("ResumeField", backref="resume_paragraph", cascade="all, delete-orphan", lazy=True)


class ResumeField(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    resume_paragraph_id = db.Column(db.Integer, db.ForeignKey('resume_paragraph.id'), nullable=False)
    key = db.Column(db.String(50), nullable=False)    # مثل title, description, date
    value = db.Column(db.Text, nullable=True)
    is_visible = db.Column(db.Boolean, default=True)

class NavigationLink(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    label = db.Column(db.String(100), nullable=False)         # مثل: Home
    icon = db.Column(db.String(10), default="")               # مثل: 🏠
    endpoint = db.Column(db.String(100), nullable=False)      # مثل: main.home
    order = db.Column(db.Integer, default=0)
    is_visible = db.Column(db.Boolean, default=True)


class LanguageOption(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    code = db.Column(db.String(10), nullable=False, unique=True)  # مثل: en, ar, de
    name = db.Column(db.String(50), nullable=False)               # مثل: English, العربية
    order = db.Column(db.Integer, default=0)
    is_visible = db.Column(db.Boolean, default=True)
