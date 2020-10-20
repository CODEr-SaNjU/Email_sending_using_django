from django.urls import path
from . import views

urlpatterns = [
    # path('compose/', views.EmailAttachementView.as_view(),name='emailattachementview'),
    path('',views.Home_page,name="Home_page")
]