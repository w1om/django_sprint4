# blogicum/users/views.py
from django.contrib.auth import get_user_model, login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, UpdateView
from django.urls import reverse_lazy, reverse
from .forms import CustomUserCreationForm, ProfileEditForm

User = get_user_model()


class RegistrationView(CreateView):
    form_class = CustomUserCreationForm
    template_name = "registration/registration_form.html"
    success_url = reverse_lazy("blog:index")

    def form_valid(self, form):
        response = super().form_valid(form)
        # Сразу авторизуем пользователя после успешной регистрации
        login(self.request, self.object)
        return response


class ProfileEditView(LoginRequiredMixin, UpdateView):
    model = User
    form_class = ProfileEditForm
    template_name = "users/user.html"

    def get_object(self, queryset=None):
        # Возвращаем текущего авторизованного пользователя
        return self.request.user

    def get_success_url(self):
        # После редактирования возвращаем пользователя в его профиль
        return reverse(
            "blog:profile", kwargs={"username": self.object.username}
        )
