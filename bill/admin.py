from django.contrib import admin
from .models import Bill
# Register your models here.

class BillAdmin(admin.ModelAdmin):
    list_display = ['bill_name', 'bill_mail_to', 'active']

admin.site.register(Bill, BillAdmin)