from django.urls import path
from . import views

app_name = 'board'

urlpatterns = [
    path('fetch_lotto/', views.fetch_lotto, name='fetch_lotto')
]