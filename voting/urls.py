from unicodedata import name
from django.urls import path
from .views import *
from .import views

urlpatterns = [
    path("", views.HomePage.as_view(), name='home'),
    path("category/nominations/<str:pk>/", views.NominationPage.as_view(), name="nomination"),
    path("vote/", views.submit_vote, name="vote"),

    path("administrator/login/", views.AdminAuth.as_view(), name="login"),
    path("administrato/dashboard/", views.Dashboard.as_view(), name="dashboard"),

    path("tmsa/nomination/", views.CreateNominations.as_view(), name="nominees"),
    path(r'success/$', views.success, name='success')
    
    # addNomination
]
