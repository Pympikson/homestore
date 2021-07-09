from django.urls import path

from . import views

urlpatterns = [
  path('contact', views.contact, name='contact'),
  path('editinq', views.editinq, name='editinq'),
  path('delinq', views.delinq, name='delinq'),
  path('editinq/<int:id>', views.editinq, name='editinq'),
  path('delinq/<int:id>', views.delinq, name='delinq'),
]