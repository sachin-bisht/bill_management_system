import datetime
from celery import shared_task, task
from celery.schedules import crontab

from bill.models import Bill
from bill.contollers import sentmail, ok



@shared_task
def monthly_bill_reminder(due_date=None):

    now = datetime.datetime.now()
    mail_to = "bshtschn@gmail.com"

    bills = Bill.objects.filter(bill_due_date=now.day, bill_time=now.hour)
    data = {}
    for bill in bills:
        status = sentmail(mail_to, bill.bill_name, bill.bill_amount)
        data[bill.bill_name] = status
    return data


