from django.urls import path
from . import views

urlpatterns = [
    path("", views.home_view, name="home"),
    path("dashboard/", views.dashboard_view, name="dashboard"),
    path("qualities/", views.qualities_view, name="qualities"),
    path("story/", views.story_view, name="story"),
    path("letter/", views.letter_view, name="letter"),
    path("unlock/", views.unlock_view, name="unlock"),
    path("lock/", views.lock_view, name="lock"),
]
