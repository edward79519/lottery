from django import forms
from .models import AwardList


class AwardModelForm(forms.ModelForm):
    class Meta:
        model = AwardList
        fields = ['emp', 'prize']
        widgets = {
            'emp': forms.HiddenInput(),
            'prize': forms.HiddenInput(),
        }