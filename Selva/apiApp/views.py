from django.shortcuts import render, redirect
from authApp.models import Ranger
from authApp.forms import RangerForm

# Create your views here.

def get_ranger_uuid(request):
    if request.method == 'POST':
        ranger_name = request.POST.get('name')
        try:
            ranger = Ranger.objects.get(name=ranger_name)
            return render(request, 'auth/admin_page.html', {'ranger': ranger})
        except Ranger.DoesNotExist:
            form = RangerForm()
            return render(request, 'auth/admin_page.html', {'error_not_found': True}, {'form':form})

    return render(request, 'auth/admin_page.html')

def ranger_reg(request):
    if request.method == 'POST':
        form = RangerForm(request.POST)
        if form.is_valid():
            ranger = form.save()
            form = RangerForm()
            return redirect('admin_page')
    else:
        form = RangerForm()
    return render(request, 'auth/admin_page.html')

