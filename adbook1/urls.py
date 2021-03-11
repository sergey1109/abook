from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add-contact/', views.AddContact, name= 'add-contact'),
    path('profile/<str:pk>', views.ContactProfile, name= 'contact-profile'),
    path('edit-contact/<str:pk>', views.EditContact, name='edit-contact'),
    path('delete/<str:pk>', views.DeleteContact, name = 'delete-contact'),
]