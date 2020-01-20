from django.urls import path
from . import views

urlpatterns = [
    path('', views.EmailAttachementView.as_view(),name='emailattachementview'),
]