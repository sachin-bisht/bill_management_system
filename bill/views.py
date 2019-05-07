from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Bill
from .forms import BillForm

from django.http import HttpResponse
from django.contrib.auth import login, authenticate
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from django.contrib.auth.models import User

def bill_list(request):
    bills = Bill.objects.all()

    return render(request, 'bill/bill_list.html', {'bills': bills})

def bill_detail(request, pk=None):
    bill = get_object_or_404(Bill, pk=pk)

    return render(request, 'bill/bill_detail.html', {'bill': bill})

def bill_new(request):
    if request.method == 'POST':
        form = BillForm(request.POST)
        if form.is_valid():
            bill = form.save()
            bill.save()
            return redirect('bill_detail', pk=bill.pk)
    else:
        form = BillForm()
    return render(request, 'bill/bill_edit.html', {'form': form})

def bill_edit(request, pk):
    bill = get_object_or_404(Bill, pk=pk)
    if request.method == "POST":
        form = BillForm(request.POST, instance=bill)
        if form.is_valid():
            bill = form.save()
            bill.save()
            return redirect('bill_detail', pk=bill.pk)
    else:
        form = BillForm(instance=bill)
    return render(request, 'bill/bill_edit.html', {'form': form})