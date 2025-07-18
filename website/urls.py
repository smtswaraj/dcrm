from django.urls import path
from . import views

urlpatterns = [
    path('',views.home, name='home'),
    path('logout/',views.logout_user, name='logout'),
    path('register/',views.register_user, name='register'),
    path('record/<int:pk>',views.customer_record, name='record'),
    path('delet_record/<int:pk>',views.delet_record, name='delet_record'),
    path('add_record/',views.add_record, name='add_record'),
    path('update_record/<int:pk>',views.update_record, name='update_record'),
]