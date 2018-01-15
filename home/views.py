from django.shortcuts import render


def home(request):
    return render(request, "home/homepage.html")


def investors(request):
    return render(request, "home/investors.html")


def about(request):
    return render(request, "home/about.html")


def partnerships(request):
    return render(request, "home/partnerships.html")


def become_instructor(request):
    return render(request, "home/become_instructor.html")
