from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login,logout
from .models import Ranger
from .forms import RangerForm

# Create your views here.

def login(request):
    return render(request, 'auth/auth_view.html')

def login_view(request):
    
    if request.method == 'POST':
        ranger_name = request.POST.get('name')
        ranger_uuid = request.POST.get('uuid')

        try:
            ranger = Ranger.objects.get(name=ranger_name, uuid=ranger_uuid)
            print(ranger)
            return render(request, 'home.html', {'ranger': ranger}) 
        except Ranger.DoesNotExist:
            return render(request, 'auth/auth_view.html', {'error_invalid': True})

    return render(request, 'auth/auth_view.html.html')

def admin_page(request):
    form = RangerForm()
    
    return render(request, 'auth/admin_page.html', {'form':form})