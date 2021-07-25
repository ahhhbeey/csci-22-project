from django.forms import ModelForm
from .models import Customer, Food, Order

class FoodForm(ModelForm):
    class Meta:
        model = Food
        fields = ['name', 'description', 'price']
        