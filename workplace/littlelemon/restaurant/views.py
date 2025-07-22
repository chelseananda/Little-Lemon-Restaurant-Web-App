# from django.http import HttpResponse
from django.shortcuts import render
from .forms import BookingForm
from .models import Menu



# Create your views here.
def home(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def book(request):
    form = BookingForm()
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
    context = {'form':form}
    return render(request, 'book.html', context)

# creating view for menu
def menu(request):
    menu_items = Menu.objects.all().order_by('name')
    return render(request, 'menu.html', {'menu': menu_items})

#view for displaying menu items
def display_menu_item(request, pk=None):
    if pk:
        menu_item = Menu.objects.get(pk=pk)
    else:
        menu_item = ""
    return render(request, 'menu_item.html', {"menu_item": menu_item})