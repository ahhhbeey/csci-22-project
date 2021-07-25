from django.urls import path
from . import views  # from . means look into the same folder of this current file

app_name = 'webkiosk'
urlpatterns = [
    path('', views.index, name='index'),  # 127.0.0.1:8000/webkiosk
    path('food/', views.listfood, name='food-list'),
    path('food/new/', views.createfood, name='food-create'),
    path('food/<int:pk>/', views.detailfood, name='food-detail'),
    path('food/<int:pk>/edit/', views.updatefood, name='food-update'),
    path('food/<int:pk>/delete/', views.deletefood, name='food-delete')
    # path('testview/', views.tv), # 127.0.0.1:8000/webkiosk/testview
]

# webkiosk/food/1
