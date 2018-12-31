from django.urls import path, include
from .views import *

urlpatterns = [
    path('',index, name='index'),
    path('display_laptop', display_laptop,name='display_laptop'),
    path('display_desktop', display_desktop,name='display_desktop'),
    path('display_mobile', display_mobile,name='display_mobile'),
    path('add_laptop', add_laptop, name='add_laptop'),
    path('add_desktop', add_desktop, name='add_desktop'),
    path('add_mobile', add_mobile, name='add_mobile'),
    # path('first/',home, name='home'),
]