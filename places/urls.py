from django.urls import path
from .views import *

app_name = 'places'

urlpatterns = [
    path('list/', PlaceListView.as_view(), name='list'), 
    path('detail/<int:id>/', PlaceDetailView.as_view(), name='detail'), 
    path('<int:id>/comment/', AddCommentView.as_view(), name='add_comment'), 
    path('place/comment/<int:comment_id>/update/', update_comment, name='update_comment'),
    path('place/comment/<int:comment_id>/delete/', delete_comment, name='delete_comment'),
]