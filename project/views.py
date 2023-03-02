from django.shortcuts import render
from django.http import HttpResponse
from .models import OrderHistory
# Create your views here.

def home(request):

    singular = OrderHistory.objects.all()

    return render(request, 'orderdetails.html',{'singular':singular})

