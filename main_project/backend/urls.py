from django.urls import path
from . import views

urlpatterns = [
    # path('compose/', views.EmailAttachementView.as_view(),name='emailattachementview'),
    path('Home',views.Home_page,name="Home_page"),
    path('',views.inbox,name="inbox")
]