from django.contrib import admin
from django.urls import path
from .views import PrimeiraView, EditView, DeleteView, login

from django.conf.urls import include
from . import views
from cadastros.apis import *

urlpatterns = [

    path('primeira-view/',PrimeiraView, name='primeira-view'),
    path('edit-view/<int:pk>/',EditView, name='edit-view'),
    path('delete-view/<int:pk>/',DeleteView, name='delete-view'),


    path('',views.login,name='index'),
    path('index',views.login,name='index'),

    path('login', views.do_login, name='login'),

    path('api/', include([

        path('api-principal', PrincipalAPI.as_view(), name='api-principal'),
        path('api-post', PessoaPostAPI.as_view(), name='api-post'),
        path('api-delete', PessoaDeleteAPI.as_view(), name='api-delete'),


    ])),
    
]
