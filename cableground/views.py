from ast import Expression
from operator import concat
from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.contenttypes.models import ContentType
from tags.models import TaggedItem, TaggedItemManager
from django.db import transaction
from django.db.models import Q,F,Value,Func,Count,ExpressionWrapper,DecimalField
from django.db.models.aggregates import Sum,Avg,Count,Max,Min
from store.models import Box, Channels,Customer

# Create your views here.

def say_hello(request):
   with transaction.atomic():
      customer = Customer()
      customer.id = 60
      customer.name = 'vivek'
      customer.address = 'girinagar , banglore'
      customer.number = '9292929292'
      customer.payment_status = True
      customer.last_payment_date = '2022-08-04'
      customer.incharge = 'A'
      customer.save()

      box = Box()
      box.box_no = '767676776776'
      box.customer = Customer(pk = 70)
      box.save()

   return render(request,'hello.html')
   



