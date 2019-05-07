from django import forms

from .models import Bill

class BillForm(forms.ModelForm):

    class Meta:
        model = Bill
        fields = (
            'bill_name',
            'bill_amount',
            'bill_due_date',
            'bill_time',
        )