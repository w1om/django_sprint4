# blogicum/users/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path(
        "registration/", views.RegistrationView.as_view(), name="registration"
    ),
    path(
        "edit_profile/",
        views.ProfileEditView.as_view(),
        name="edit_profile",  # <--- ВОТ ЗДЕСЬ ИЗМЕНИЛИ ИМЯ
    ),
]
