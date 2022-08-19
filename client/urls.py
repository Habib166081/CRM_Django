from django.urls import path
from . import views

urlpatterns = [
    path('client/<str:pk>',views.list_client,name='client'),

]

