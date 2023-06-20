from django.urls import path
from .views import StocksList, InvestList, InvestDetail, InvestCreate, InvestUpdate, InvestDelete, Login, Register
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('login/', Login.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('register/', Register.as_view(), name='register'),
    path('', InvestList.as_view(), name='investments'),
    path('stocks/', StocksList.as_view(), name='stocks_list'),
    path('invest/<int:pk>/', InvestDetail.as_view(), name='invest'),
    path('invest-create/', InvestCreate.as_view(), name='invest-create'),
    path('invest-update/<int:pk>/', InvestUpdate.as_view(), name='invest-update'),
    path('invest-delete/<int:pk>/', InvestDelete.as_view(), name='invest-delete'),
    path('investor-data/', Register.getData1, name='investor-data'),
    path('add-perfil/', Register.addPerfil, name='add-perfil'),
    path('stocks-data/', StocksList.getData, name='stocks_data'),
    path('add-stock/', StocksList.addStock, name='add_stock')
]