from django import forms
from ..models.submit import Submit


class SubmitForm(forms.ModelForm):
    class Meta:
        model = Submit
        fields = ('language', 'code')

        widgets = {
            'language': forms.Select(attrs={'class': 'form-control'}),
            'code': forms.Textarea(attrs={'class': 'form-control', 'name': 'editor', 'style': 'display: none;'}),
        }