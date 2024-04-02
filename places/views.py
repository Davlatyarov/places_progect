from django.shortcuts import render
from .models import *
from django.views.generic import ListView, DeleteView, DetailView
from .forms import *
from django.core.paginator import Paginator
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin 
from django.urls import reverse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST

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
        paginator = Paginator(comments, 2)  # Пагинация 

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

        return render(request, 'places/detail.html', {"form":comment_form, "place":place})

@login_required
def update_comment(request, comment_id):
    comment = get_object_or_404(PlaceComment, pk=comment_id)
    
    if request.method == 'POST':
        form = PlaceCommentForm(request.POST, instance=comment)
        if form.is_valid():
            form.save()
            place = comment.place
            return redirect('places:detail', id=place.id)  
    else:
        form = PlaceCommentForm(instance=comment)
    
    return render(request, 'places/update_comment.html', {'form': form})

@login_required
def delete_comment(request, comment_id):
    comment = get_object_or_404(PlaceComment, pk=comment_id)
    
    if request.method == 'POST':
        comment.delete()
        # Redirect to a relevant page after deletion
        return redirect('places:detail', id=comment.place.id)
    
    return render(request, 'places/delete_comment.html', {'comment': comment})