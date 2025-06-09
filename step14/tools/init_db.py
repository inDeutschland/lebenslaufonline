import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from __init__ import create_app

from models.models import db, Section, Setting

app = create_app()

with app.app_context():
    db.drop_all()
    db.create_all()

    # إدخال بيانات أولية
    sections = [
        "Profil", "Karriereziel", "Bevorzugte Bereiche",
        "Berufserfahrung", "Qualifikationen", "Technische Fähigkeiten",
        "Sprachen", "Projekte", "Links", "Interessen"
    ]
    

    for title in sections:
        db.session.add(Section(title=title, content=""))

    db.session.add(Setting(key="section_title_css", value="{'font-size': '18px', 'color': '#000'}"))
    db.session.commit()

    print("✅ Datenbank initialisiert und mit Beispieldaten gefüllt.")
