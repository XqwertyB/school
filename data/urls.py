# myapp/urls.py
from django.urls import path
from data import views
from .views import feedback_view

urlpatterns = [
    path('feedback/', feedback_view),
    path('news/', views.NewsView.as_view(),),
    path('art/', views.ArtView.as_view(),),


]
