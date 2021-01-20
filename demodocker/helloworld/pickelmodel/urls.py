from django.urls import path
from . import views

urlpatterns = [
    path('loadmodel/', views.savemodeltopickel, name='loadmodel'),
]