import datetime

from django.db import models
from bill_management.base_model import BaseModel
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.

class BillManager(models.Manager):
    def active(self):
        return super.get_queryset().filter(active=True)

    def expired(self):
        return super.get_queryset().filter(active=False)

class Bill(BaseModel):
    bill_name = models.CharField(max_length=300, help_text='Name of the Bill (Office Rent, Electricity Bill, etc.)')
    bill_amount = models.DecimalField(max_digits=20, decimal_places=5, null=True, blank=True)
    bill_due_date = models.IntegerField(
        validators=[MaxValueValidator(28), MinValueValidator(1)],
        help_text='Enter date b/w 1 and 28'
    )
    bill_mail_to = models.EmailField(default='sachinbisht939@gmail.com') #aman@allincall.in
    bill_time = models.IntegerField(
        validators=[MaxValueValidator(23), MinValueValidator(0)],
        help_text='Enter value in 24 hour format')
    active = models.BooleanField(default=True)

    objects = models.Manager()
    BillManager = BillManager()

    def __str__(self):
        return str(self.bill_name)
