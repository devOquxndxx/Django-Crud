from django.urls import path 
from . import views

urlpatterns = [
    path('', views.home, name='home'), 
    path('login/', views.login_user, name='login'),
    path('register/', views.register_user, name='register'),
    path('logout/', views.logout_user, name='logout'),
    path('record/<int:pk>', views.customer_record, name='record'), # Esta función define la vista de un registro específico (customer_record) del sitio.
    path('delete_record/<int:pk>', views.delete_record, name='delete_record'),
    path('add_record/', views.add_record, name='add_record'),
    path('update_record/<int:pk>', views.update_record, name='update_record'),

]