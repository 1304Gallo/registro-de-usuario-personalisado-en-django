from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.contrib.auth.views import LoginView, LogoutView
from Usuario.forms import CustomUserCreationForm
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.models import User


# Vista personalizada para el registro de usuarios
class CustomSignupView(CreateView):
    form_class = CustomUserCreationForm
    template_name = 'registration/signup.html'
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        # Verificar si el  usuario ya existe
        username = form.cleaned_data.get('username')
        print('El nombre de usuario ingresado es:', username)
        if User.objects.filter(username=username).exists():
            messages.error(self.request, 'El nombre de usuario ya está en uso.')
            return self.form_invalid(form)

        # Guardar el usuario en la base de datos
        user = form.save()


        # Mensajes de depuración
        print("Formulario:", form.cleaned_data)
        print("Usuario creado:", user)

        response = super().form_valid(form)
        print("Respuesta de redireccionamiento:", response)
        return response

    def form_invalid(self, form):
        # Agrega un mensaje de error adicional si el formulario es inválido debido a un nombre de usuario duplicado.
        if 'username' in form.errors:
            messages.warning(self.request, 'El nombre de usuario ya está en uso.')
        return super().form_invalid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Registro de usuario'
        return context

    def get_form_class(self):
        return CustomUserCreationForm

# Vista personalizada para el inicio de sesión
class CustomLoginView(LoginView):
    template_name = 'registration/login.html'

    def form_valid(self, form):
        messages.success(self.request, 'Usted se ha autenticado correctamente')
        response = super().form_valid(form)
        next_url = self.request.POST.get('next')
        if next_url:
            return redirect(next_url)
        else:
            return response


# Vista personalizada para el cierrede sesión
class CustomLogoutView(LogoutView):
    pass