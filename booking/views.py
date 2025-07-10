
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from .models import Hotel, Room, Booking
from datetime import date

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Log the user in after registration
            return redirect('home')  # redirect to homepage or dashboard
    else:
        form = UserCreationForm()
    return render(request, 'booking/register.html', {'form': form})

def home(request):
    hotels = Hotel.objects.all()
    return render(request, 'booking/home.html', {'hotels': hotels})


def search_rooms(request):
     rooms = []
     city = ''
     if request.method == 'POST':
        city = request.POST.get('city')
        rooms = Room.objects.filter(hotel__city__icontains=city, is_available=True)
     return render(request, 'booking/search.html', {'rooms': rooms, 'city': city})

@login_required
def book_room(request, room_id):
    room = get_object_or_404(Room, id=room_id)
    if request.method == 'POST':
        check_in = request.POST['check_in']
        check_out = request.POST['check_out']
        Booking.objects.create(user=request.user, room=room, check_in=check_in, check_out=check_out)
        room.is_available = False
        room.save()
        return redirect('my_bookings')
    return render(request, 'booking/book_room.html', {'room': room})

def view_price(request, room_id):
    room = get_object_or_404(Room, id=room_id)
    return render(request, 'booking/price.html', {'room': room})

def register_user(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'booking/register.html', {'form': form})

def login_user(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'booking/login.html', {'form': form})

def logout_user(request):
    logout(request)
    return redirect('home')

@login_required
def view_bookings(request):
    bookings = Booking.objects.filter(user=request.user)
    return render(request, 'booking/my_bookings.html', {'bookings': bookings})
