from django.shortcuts import render,redirect
from .forms import InfoForm
from .models import Info
# Create your views here.

def add_info(request):
    if request.method == 'POST':
        form = InfoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('show_info')
    else:
        form = InfoForm()
    return render(request,'myapp/add_info.html', {'form': form})
 
def show_info(request):
    info = Info.objects.last()
    return render(request,'myapp/show_info.html' , {'info': info})