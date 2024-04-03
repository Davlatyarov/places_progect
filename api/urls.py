from django.urls import path
from .views import PlaceDetailApiView, PlacesApiView, ReviewsApiView, LoginApiView
app_name = 'api'

urlpatterns = [
    path('place_detail/<int:id>/', PlaceDetailApiView.as_view() , name='place_detail'),
    path('places/', PlacesApiView.as_view() , name='places'),
    path('places/<int:id>', PlacesApiView.as_view(), name="places"),
    path('reviews/', ReviewsApiView.as_view() , name='reviews'),
    path('login/', LoginApiView.as_view() , name='login'),
    
    
]