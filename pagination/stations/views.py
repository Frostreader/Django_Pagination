from django.shortcuts import render, redirect
from django.urls import reverse
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
import csv


def index(request):
    return redirect(reverse('bus_stations'))


def bus_stations(request):
    page_number = request.GET.get('page')
    if page_number is None:
        page_number = 1

    with open('data-398-2018-08-30.csv', encoding='utf-8-sig', newline='') as file:
        reader = csv.DictReader(file)
        stations = list(reader)

    paginator = Paginator(stations, 10)

    try:
        page = paginator.page(page_number)
    except PageNotAnInteger:
        page = paginator.page(1)
    except EmptyPage:
        page = paginator.page(paginator.num_pages)

    context = {
        'bus_stations': page,
        'page': page,
    }
    return render(request, 'stations/index.html', context)