from django.shortcuts import render


def index(request):
    """Home page app Learning Logs."""
    return render(request, "learning_logs/index.html")
