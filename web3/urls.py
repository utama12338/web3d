# web3/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # URL pattern เริ่มต้นสำหรับหน้าหลัก (เช่น index.html)
    path('login/', views.login_view, name='login'),  # URL pattern สำหรับหน้า Login
    path('table/', views.table_view, name='table_view'),  # URL pattern สำหรับหน้า table (ตัวอย่างเท่านั้น)
    path('', views.product_list, name='product_list'),
    path('product/<int:pk>/', views.product_list, name='product_detail'),
]

