from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib import messages
from functools import wraps

from .models import SiteSetting, Question, Quality, Memory, LoveLetter


def passcode_required(view_func):
    """
    Decorator to protect views if passcode protection is enabled in SiteSetting.
    """
    @wraps(view_func)
    def _wrapped_view(request, *args, **kwargs):
        settings_obj = SiteSetting.get_settings()
        if settings_obj.is_passcode_protected:
            if not request.session.get("site_unlocked", False):
                return redirect(reverse("unlock"))
        return view_func(request, *args, **kwargs)
    return _wrapped_view


def unlock_view(request):
    """
    Passcode verification page when privacy lock is enabled.
    """
    settings_obj = SiteSetting.get_settings()
    if not settings_obj.is_passcode_protected or request.session.get("site_unlocked", False):
        return redirect("home")

    error_msg = None
    if request.method == "POST":
        entered_passcode = request.POST.get("passcode", "").strip()
        if entered_passcode.lower() == settings_obj.passcode.strip().lower():
            request.session["site_unlocked"] = True
            messages.success(request, f"Welcome to our world, {settings_obj.girlfriend_name}! ❤️")
            next_url = request.GET.get("next") or reverse("home")
            return redirect(next_url)
        else:
            error_msg = "That passcode didn't match. Try again, sweetheart! 💕"

    return render(request, "love_site/unlock.html", {
        "settings_obj": settings_obj,
        "error_msg": error_msg,
    })


def lock_view(request):
    """
    Manually lock the site again if passcode protection is on.
    """
    if "site_unlocked" in request.session:
        del request.session["site_unlocked"]
    return redirect("unlock")


@passcode_required
def home_view(request):
    """
    Landing page: 'Our Little World'
    """
    settings_obj = SiteSetting.get_settings()
    questions_count = Question.objects.filter(is_active=True).count()
    qualities_count = Quality.objects.filter(is_active=True).count()
    memories_count = Memory.objects.filter(is_active=True).count()
    has_letter = LoveLetter.objects.filter(is_active=True).exists()

    context = {
        "settings_obj": settings_obj,
        "questions_count": questions_count,
        "qualities_count": qualities_count,
        "memories_count": memories_count,
        "has_letter": has_letter,
        "current_page": "home",
    }
    return render(request, "love_site/home.html", context)


@passcode_required
def dashboard_view(request):
    """
    Interactive questions dashboard: 'Questions About Us'
    """
    questions = Question.objects.filter(is_active=True).order_by("display_order", "created_at")
    context = {
        "questions": questions,
        "current_page": "dashboard",
    }
    return render(request, "love_site/dashboard.html", context)


@passcode_required
def qualities_view(request):
    """
    'Things I Love About You 💕' section
    """
    qualities = Quality.objects.filter(is_active=True).order_by("display_order", "title")
    context = {
        "qualities": qualities,
        "current_page": "qualities",
    }
    return render(request, "love_site/qualities.html", context)


@passcode_required
def story_view(request):
    """
    'Our Story, From the Beginning to Today ❤️' chronological timeline
    """
    memories = Memory.objects.filter(is_active=True).order_by("display_order", "date", "id")
    context = {
        "memories": memories,
        "current_page": "story",
    }
    return render(request, "love_site/story.html", context)


@passcode_required
def letter_view(request):
    """
    'What I Feel for You 💌' personal love letter page
    """
    letter = LoveLetter.objects.filter(is_active=True).first()
    context = {
        "letter": letter,
        "current_page": "letter",
    }
    return render(request, "love_site/letter.html", context)
