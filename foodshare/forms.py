from django import forms
from .models import FoodPost

class FoodPostForm(forms.ModelForm):
    class Meta:
        model = FoodPost
        exclude = ['user']  # ✅ Exclude user – it will be set in the view manually
