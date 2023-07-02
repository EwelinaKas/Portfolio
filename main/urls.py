from django.urls import path

from main import views

app_name = 'main'

urlpatterns = [
    path('', views.home, name='home'),

    # PHOTOS
    path('portraits/', views.portraits_view, name='portraits'),
]
