from django.urls import path

from .views import verify_view

urlpatterns = [
    path('', verify_view, name='verify_view'),
]