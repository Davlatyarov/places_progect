from django.shortcuts import render
from .models import *
from django.views.generic import ListView, DeleteView, DetailView
from .forms import *
from django.core.paginator import Paginator
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin 
from django.shortcuts import redirect
from django.urls import reverse
class PlaceListView(ListView):
    template_name = 'places/list.html'
    queryset = Place.objects.all()
    context_object_name = 'places'
    paginate_by = 2


    
class PlaceDetailView(DeleteView):
    template_name = 'places/detail.html'
    queryset = Place.objects.all()
    context_object_name = 'place'
    pk_url_kwarg = 'id'


class PlaceDetailView(DetailView):
    template_name = 'places/detail.html'
    queryset = Place.objects.all()
    context_object_name = 'place'
    pk_url_kwarg = 'id'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        place = self.get_object()
        place_comment_form = PlaceCommentForm()
        
        comments = place.reviews.all().order_by('-created_at')
        paginator = Paginator(comments, 1)  # Пагинация 

        page_number = self.request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        

        context['page_obj'] = page_obj
        context['form'] = place_comment_form
        return context


class AddCommentView(LoginRequiredMixin, View):

    def post(self, request, id):

        place = Place.objects.get(id=id)
        comment_form = PlaceCommentForm(data=request.POST)

        if comment_form.is_valid():
            PlaceComment.objects.create(
                place=place,
                user=request.user,
                comment=comment_form.cleaned_data['comment'],
                stars_given=comment_form.cleaned_data['stars_given']
            )
            return redirect(reverse('places:detail', kwargs={"id": place.id}))

        return render(request, 'places/detail.ntml', {"form":comment_form, "place":place})
