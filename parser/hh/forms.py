from django import forms
from .models import Vacancy

class VacancyForm(forms.ModelForm):
    class Meta:
        model = Vacancy
        fields = (
            "title",
            "salary",
            "expirience",
            "area",
            "url",
        )
        widgets = {
            'title': forms.TextInput,
        }