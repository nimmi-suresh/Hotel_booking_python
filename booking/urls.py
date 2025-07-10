from django.contrib.auth import views as auth_views
from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='booking/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='home'), name='logout'),
    path('', views.home, name='home'),
    path('search/', views.search_rooms, name='search_rooms'),
    path('booking/<int:room_id>/', views.book_room, name='book_room'),
    path('price/<int:room_id>/', views.view_price, name='view_price'),
    path('register/', views.register_user, name='register'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('mybookings/', views.view_bookings, name='my_bookings'),
    path('', views.home, name='home'),
    path('search/', views.search_rooms, name='search_rooms'),
    path('book/<int:room_id>/', views.book_room, name='book_room'),
    path('my-bookings/', views.view_bookings, name='my_bookings'),
    path('register/', views.register, name='register'),
]
