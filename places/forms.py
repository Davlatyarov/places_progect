from django import forms
from .models import PlaceComment

class PlaceCommentForm(forms.ModelForm):
    stars_given = forms.IntegerField(max_value=5,min_value=1)

    class Meta:
        model = PlaceComment
        fields = ('comment', 'stars_given')
