from django.shortcuts import render, redirect
# Create your views here.

from .forms import RegisterForm
def register(request):
    if request.method=="POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success')
    else:
        form = RegisterForm()
    return render(request, 'register.html', {'form': form})

def index(request):
    return render(request, 'index.html')
