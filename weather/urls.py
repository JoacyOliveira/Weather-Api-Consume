from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('',views.index),
    path('delete/<city_name>/',views.delete_city,name='delete_city'),
    path('admin/', admin.site.urls),
]
