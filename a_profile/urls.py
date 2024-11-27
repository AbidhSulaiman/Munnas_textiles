from django.urls import path
from .views import profile_view, profile_edit_view, address_edit_view

urlpatterns = [
    path('profile_view/', profile_view, name='profile_view'),
    path('profile_edit/', profile_edit_view, name='profile_edit'),
    path('address_edit/', address_edit_view, name='address_edit'),
]
