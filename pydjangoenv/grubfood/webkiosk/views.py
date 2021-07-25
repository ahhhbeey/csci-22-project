from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages

from .models import Customer, Food, Order
from .forms import FoodForm

# Create your views here.


def index(request):
    # return HttpResponse('<p>Welcome to the GrubFood Web Kiosk!</p>')
    return render(request, 'webkiosk/welcome.html')


def listfood(request):
    context = {
        'foodlist': Food.objects.all(),
        'testitem': 'chair'
    }
    return render(request, 'webkiosk/food.html', context)


def createfood(request):
    if request.method == 'GET':  # just getting the data -- like when you're just visiting the form page
        form = FoodForm()  # you create an empty food form
    elif request.method == 'POST':  # when you click submit in the form, it makes a POST request
        # insert new food record, it will contain the data that will be typed into the form
        form = FoodForm(request.POST)
        if form.is_valid():  # if the form is valid
            form.save()  # we save the form; adds a record to the database
            return redirect('webkiosk:food-list')

    context = {'form': form}
    return render(request, 'webkiosk/food_form.html', context)


def detailfood(request, pk):  # pk is a primary key which is a parameter in urls
    food = Food.objects.get(id=pk)

    context = {'food': food}
    return render(request, 'webkiosk/food_detail.html', context)


def updatefood(request, pk):
    food = Food.objects.get(id=pk)
    if request.method == 'GET':
        form = FoodForm(instance=food)
    elif request.method == 'POST':
        # instance is to specify which food record we want to update
        form = FoodForm(request.POST, instance=food)
        if form.is_valid():
            form.save()
            messages.success(request, 'Food record successfully updated.')

    context = {'form': form}
    return render(request, 'webkiosk/food_form.html', context)


def deletefood(request, pk):
    food = Food.objects.get(id=pk)
    if request.method == 'GET':
        context = {'food': food}
        return render(request, 'webkiosk/food_delete.html', context)
    elif request.method == 'POST':
        food.delete()
        return redirect('webkiosk:food-list')
