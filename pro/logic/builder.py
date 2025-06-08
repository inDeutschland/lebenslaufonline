import json
from ..models.models import Setting

def get_css_setting(key, default=""):
    setting = Setting.query.filter_by(key=key).first()
    if setting:
        try:
            css_dict = json.loads(setting.value.replace("'", '"'))
            return "; ".join(f"{k}: {v}" for k, v in css_dict.items())
        except:
            return default
    return default
