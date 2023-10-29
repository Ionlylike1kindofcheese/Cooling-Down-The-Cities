from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.signin, name='login'),
    path('logout/', views.signout, name='signout'),
    path('signup/', views.signup, name='signup'),
    path('privatepolicy/', views.privatePolicy, name='privatepolicy'),
    path('dashboard/', views.dashboard, name='dashboard'),
]