from django.urls import path

from .views import ListTaskTracker, DetailTaskTracker

urlpatterns = [
    path('', ListTaskTracker.as_view()),
    path('<int:pk>/', DetailTaskTracker.as_view()),
]
