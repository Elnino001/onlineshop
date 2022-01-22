from django.urls import path
from . import views

app_name = 'gallery'
urlpatterns = [
    path('', views.art_list, name='art_list'),
    path('<slug:category_slug>/', views.art_list, name='art_list_by_category'),
    path('<int:id>/<slug:slug>/', views.art_detail, name='art_detail'),

    
]
