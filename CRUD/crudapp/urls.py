from django.urls import path
from . import views

urlpatterns=[
    path('',views.home),
    path('load/', views.load_form),
    path('add/', views.add, name ='add'),
    path('show/',views.show),
    path('show/edit/<int:id>',views.edit),
    path('show/edit/update/<int:id>',views.update),
    path('show/delete/<int:id>',views.delete),
    path('show/search',views.search),
]