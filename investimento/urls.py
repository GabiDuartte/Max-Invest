from django.urls import path

from . import views

app_name = 'investimento'
urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('<int:pk>/', views.CalcTot.as_view(), name='detail'),
]
