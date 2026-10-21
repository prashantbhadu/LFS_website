from .models import SiteSetting
from datetime import date


def site_settings_context(request):
    """
    Context processor to inject site settings and days-together count across all templates.
    """
    settings_obj = SiteSetting.get_settings()
    days_together = None
    if settings_obj.relationship_start_date:
        delta = date.today() - settings_obj.relationship_start_date
        if delta.days >= 0:
            days_together = delta.days

    return {
        "site_settings": settings_obj,
        "days_together": days_together,
        "is_unlocked": request.session.get("site_unlocked", False),
    }
