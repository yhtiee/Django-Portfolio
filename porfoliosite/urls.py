from django.urls import path, re_path
from . import views
urlpatterns = [
    path("", views.Homepage, name="homepage"),
    # path("virtual/", views.Virtual),
    path("projects", views.Projects, name="projects"),
    path("skills", views.Skills, name="skills"),
    path("contact", views.Contact, name="contact"),
    path("cv", views.Cv, name="cv")
    ]