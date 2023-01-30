from django.urls import path
from . import views

app_name='homepage'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    # path('test', views.TestView.as_view(), name='Test'),
]
