from django.shortcuts import redirect
from django.views.generic import FormView
from django.contrib.auth import authenticate, login
from django.urls import reverse_lazy
from .forms import LoginForm

class LoginView(FormView):
    template_name = 'login.html'
    form_class = LoginForm
    success_url = reverse_lazy('success')

    def form_valid(self, form):
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user = authenticate(self.request, username=username, password=password)
        if user is not None:
            login(self.request, user)
            return super().form_valid(form)
        else:
            form.add_error(None, 'Invalid login credentials')
            return self.form_invalid(form)
