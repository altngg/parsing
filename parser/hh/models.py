from django.db import models

class Vacancy(models.Model):
    title = models.TextField(
        verbose_name= "Название",
    )
    salary = models.PositiveBigIntegerField(
        verbose_name='Зарплата'
    )
    expirience = models.TextField(
        verbose_name= 'Опыт работы'
    )
    area = models.TextField(
        verbose_name= 'Город'
    )
    url = models.URLField(
        verbose_name= 'Ссылка на вакансию'
    )

    class Meta:
        verbose_name = "Вакансия"
        verbose_name_plural = "Вакансии"