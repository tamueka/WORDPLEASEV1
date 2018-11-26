from django.urls import path

from users.views import LoginView, LogoutView, RegisterView

urlpatterns = [
    path('login', LoginView.as_view(), name='login'),
    path('logout', LogoutView.as_view(), name='logout'),
    path('signup', RegisterView.as_view(), name='signup'),
]