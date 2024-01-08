from django.shortcuts import render

def load_timer(request):
    return render(request, "index.html")
