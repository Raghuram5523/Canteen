from django.shortcuts import render, redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages
from .models import OrderConfirmation
# Create your views here.

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

def orderdetails(request):

    singular = OrderConfirmation.objects.all()

    return render(request, 'orderdetails.html',{'singular':singular})

def index(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        user = auth.authenticate(username = username, password = password)
        print(user)
        if user is not None:
            auth.login(request, user)
            return redirect('orderdetails')
        else:
            messages.info(request, "invalid credentials")
            return redirect('index')
    else:
        return render(request, 'index.html')

def signup(request):

    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        branch = request.POST['branch']
        collegeid = request.POST['collegeid']
        email = request.POST['email']
        age = request.POST['age']
        gender = request.POST['gender']
        phoneno = request.POST['phoneno']
        password = request.POST['password']
        cpassword = request.POST['cpassword']

        if password == cpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'Username taken')
                return redirect('signup')
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'Email taken')
                return redirect('signup')
            else:
                user = User.objects.create_user(username = username, first_name=first_name, last_name=last_name, email=email, password=password)
                user.branch = branch
                user.collegeid = collegeid
                user.age = age
                user.gender = gender
                user.phoneno = phoneno
                user.save()
                return redirect('index')
        else:
            print("password not matching")
            return redirect('signup')

    else:
        return render(request, 'signup.html')