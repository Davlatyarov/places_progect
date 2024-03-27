from django.shortcuts import render
from .models import Place
from django.views.generic import ListView, DeleteView

class PlaceListView(ListView):
    template_name = 'places/list.html'
    queryset = Place.objects.all()
    context_object_name = 'places'
    paginate_by = 1


    
class PlaceDetailView(DeleteView):
    template_name = 'places/detail.html'
    queryset = Place.objects.all()
    context_object_name = 'place'
    pk_url_kwarg = 'id'