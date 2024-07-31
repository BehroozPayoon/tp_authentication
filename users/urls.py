from django.urls import path

from .views import RegisterView, LoginView, AuthenticateView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('authenticate/', AuthenticateView.as_view(), name='authenticate'),
]
