from django.urls import path
from rtb import views

app_name = 'rtb'

urlpatterns = [
	path('', views.index, name = 'index'),
]