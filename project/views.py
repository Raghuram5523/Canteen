from django.shortcuts import render
from django.http import HttpResponse
from .models import OrderHistory
# Create your views here.

'''
def order(request):

    singular = OrderHistory.objects.all()

    return render(request, 'orderdetails.html',{'singular':singular})
'''
items = {'Biriyani':["Chicken Biriyani", "Veg Biriyani", "Fried Rice"],
             'Dessert':["Fruit Salad","Vegetable Salad","Kala Jamun"],
             'Ice_cream':["Chocolate","Strawberry","Butterscoch"],
             'Fast_food':["Noodles","French fries","Chicken munchuriya"],
             'Lunch':["Veg meals","Non-veg meals"],
             'Juices':["Banana","Apple","Kaju","Musk melon"]}

biriyani_length = list(range(len(items['Biriyani'])))
dessert_length = list(range(len(items['Dessert'])))
icecream_length = list(range(len(items['Ice_cream'])))
fastfood_length = list(range(len(items['Fast_food'])))
lunch_length = list(range(len(items['Lunch'])))
juices_length  =list(range(len(items['Juices'])))

def inventory(request):

    return render(request, 'inventory.html',{'items':items,'biriyani_length':biriyani_length,'dessert_length':dessert_length,'icecream_length':icecream_length,'fastfood_length':fastfood_length,'lunch_length':lunch_length,'juices_length':juices_length})