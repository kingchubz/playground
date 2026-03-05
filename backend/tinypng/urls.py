from django.urls import path

from . import views

urlpatterns = [
    path('time/', views.curr_date, name='current_time'),
]