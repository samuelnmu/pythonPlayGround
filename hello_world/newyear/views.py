from django.shortcuts import render
import datetime

def index(request):
    now = datetime.datetime.now()
    return render(request, "newyear/index.html", {
        "newyear": now.month == 1 and now.day == 1  # Check if it's New Year's Day
    })
