from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    # Add your URL patterns here
    # For example, if you have a view named 'index' in views.py
    # and you want to map the URL 'home/' to that view:
    # path('home/', views.index, name='home'),
]
