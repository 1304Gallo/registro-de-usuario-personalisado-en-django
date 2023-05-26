from django.urls import path, include
from django.contrib.auth import views as auth_views
from .views import CustomSignupView, CustomLoginView, CustomLogoutView

app_name = 'solicitud'

urlpatterns = [
    # Vista prediseñada de Django para el inicio de sesión
    path('login/', CustomLoginView.as_view(template_name='registration/login.html'), name='login'),

    # Vista prediseñada de Django para el cierre de sesión
    path('logout/', CustomLogoutView.as_view(), name='logout'),

    # Vista personalizada para el registro de usuarios
    path('signup/', CustomSignupView.as_view(), name='signup'),
]