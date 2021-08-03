from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.


class Order(models.Model):
    card = models.ForeignKey(
        'cars.car',
        on_delete=models.CASCADE,
    )

    STATUS_ORDER_ACTIVE = 'Active'
    STATUS_ORDER_DONE = 'Done'
    STATUS_ORDER_REJECT = 'Reject'

    STATUS_ORDER_CHOICE = (
        (STATUS_ORDER_ACTIVE, 'Active'),
        (STATUS_ORDER_DONE, 'Done'),
        (STATUS_ORDER_REJECT, 'Reject'),
    )

    status_order = models.CharField(
        max_length=50,
        choices=STATUS_ORDER_CHOICE,
        default=STATUS_ORDER_ACTIVE,
    )

    first_name = models.CharField(max_length=50)

    second_name = models.CharField(max_length=50)

    email = models.EmailField(max_length=50)

    phone = PhoneNumberField(
        unique=False,
        null=False,
        blank=False,
    )

    message = models.TextField(
        blank=True,
    )

    class Meta:
        verbose_name = 'Замовлення'
        verbose_name_plural = 'Замовлення'

    def __str__(self):
        return f'{self.first_name} {self.second_name}'
