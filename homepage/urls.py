from django.urls import path
from . import views
from webprofile import settings


app_name='homepage'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    
]

if settings.DEBUG:
    test_path = path('test', views.TestView.as_view(), name='Test')
    urlpatterns.append(test_path)
