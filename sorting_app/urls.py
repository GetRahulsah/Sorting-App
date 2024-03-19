# sorting_app/urls.py
# from django.urls import path
# from .views import home

# urlpatterns = [
#     path('', views.home, name='home'),
# ]


from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    # Other paths...
]