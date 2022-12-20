from django.urls import path,include
from .views import registerUser,loginPage,logoutPage,dashboard
urlpatterns = [
    path('registerUser',registerUser,name='registerUser'),
    path('login/', loginPage, name='login'),
    path('logout/', logoutPage, name='logout'),
    path('dashboard/', dashboard, name='dashboard'),
    # path('', views.dashboard, name='dashboard'),
    # path('my_orders/', views.my_orders, name='my_orders'),
    # path('edit_profile/', views.edit_profile, name='edit_profile'),
    # path('change_password/', views.change_password, name='change_password'),
    # path('order_detail/<int:order_id>/', views.order_detail, name='order_detail'),
    #
    path('registerVendor',registerUser,name='registerVendor'),
]