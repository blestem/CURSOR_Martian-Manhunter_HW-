from django.db import models


class NewsLetterModel(models.Model):
    email = models.EmailField(
        max_length=50,
        unique=True,
    )

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = 'Розсилка'
        verbose_name_plural = 'Розсилки'


