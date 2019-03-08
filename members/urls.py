from django.urls import path

from . import views

app_name = 'members'
urlpatterns = [
    path('', views.MemberIndexView.as_view(), name='index'),
    path('<int:pk>/', views.MemberDetailView.as_view(), name='detail'),
]