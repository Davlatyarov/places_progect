from django.urls import path
from .views import *

app_name = 'places'


urlpatterns = [

    path('list/', PlaceListView.as_view(), name='list'), 
    path('detail/<int:id>/', PlaceDetailView.as_view(), name='detail'), 
    
]