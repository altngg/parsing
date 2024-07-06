from django.contrib import admin

from .models import Vacancy
from .forms import VacancyForm 

@admin.register(Vacancy)
class VacancyAdmin(admin.ModelAdmin):
    list_display = ("pk", "title", "salary", "expirience", "area", "url")
    form = VacancyForm



