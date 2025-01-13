from django.shortcuts import render, redirect
from django.contrib.auth import login, logout

from .forms import CustomUserCreationForm


def register(request):
    """Registers a new user."""
    if request.method != 'POST':
        form = CustomUserCreationForm()
    else:
        form = CustomUserCreationForm(data=request.POST)

        if form.is_valid():
            new_user = form.save()
            login(request, new_user)
            return redirect('learning_logs:index')
    
    context = {'form': form}
    return render(request, 'users/register.html', context)
