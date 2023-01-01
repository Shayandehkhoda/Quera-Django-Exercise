from django.shortcuts import render, HttpResponse
from .models import Musician, Album
from django import views


class Musician_list(views.View):
    def get(self, request):
        namelist = Musician.objects.order_by('name').values_list('name', flat=True)
        return HttpResponse(f"{''.join(map(str, namelist))}")

