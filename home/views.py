from django.shortcuts import render


def home(request):
    return render(request, "home/homepage.html")


def investors(request):
    return render(request, "home/investors.html")
