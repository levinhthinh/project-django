from django.shortcuts import render,redirect
from .forms import InfoForm
from .models import Info
from .models import Book
from .models import Keyboard
# Create your views here.
def shop_content(request):
    keyboards= Keyboard.objects.all()
    return render(request,'myapp/shop_content.html',{'kbs':keyboards})

def shop_detail(request,kb_id):
    keyboard=Keyboard.objects.get(pk=kb_id)
    return render(request,'myapp/shop_detail.html',{'kb':keyboard})

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

def book_list(request):
    books= Book.objects.all()
    return render(request,'myapp/bookstore.html', {'books':books})