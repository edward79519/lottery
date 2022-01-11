from django.contrib import admin
from django.urls import path
from . import views
from .ajax import getaward

urlpatterns = [
    path('', views.index, name="Draw_index"),
    path('ajax/getaward/', getaward.luckydraw, name="GetAward"),
    path('ajax/getprizestatus/', getaward.getPrizeStauts, name="GetPrizeStatus"),
]
