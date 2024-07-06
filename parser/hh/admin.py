from django.contrib import admin

from .forms import VacancyForm
from .models import Vacancy


@admin.register(Vacancy)
class VacancyAdmin(admin.ModelAdmin):
    list_display = ("title", "salary", "expirience", "area", "url")
    form = VacancyForm
