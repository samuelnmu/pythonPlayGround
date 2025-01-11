from django.shortcuts import render
from django.shortcuts import render, redirect

# Create your views here.

tasks = ["food", "code", "Run", "Drive"]

def index(request):
    return render(request, "tasks/index.html", {
        "tasks" : tasks
    }) 


def add(request):
    if request.method == 'POST':
        # Access the submitted text from the form
        text = request.POST['text']
        # Add the task to your tasks list (or database)
        tasks.append(text)  # Assuming you want to add to the in-memory list for now
        # Redirect to the index page after successful addition (optional)
        return redirect('index')
    else:
        return render(request, "tasks/add.html")