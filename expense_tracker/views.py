from django.shortcuts import render


def home(request):
    return render(request, "home.html")

def success_page(request):
    return render(request, "success_page.html")
