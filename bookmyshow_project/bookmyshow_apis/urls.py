from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from django.conf.urls import url

urlpatterns = [
path('shows_per_city', views.list_all_movies_per_city.as_view(), name = 'shows_per_city'),
path('cinema_theatres_with_show_timings',views.cinema_theatres_with_show_timings.as_view(),name = 'cinema_theatres_with_show_timings'),
path('showtime_seats_availability',views.showtime_seats_availability.as_view(),name = 'showtime_seats_availability'),
path('booktickets1', views.booktickets, name='home'),
path('login/', auth_views.LoginView.as_view(),name='login'),
path('logout/', auth_views.LogoutView.as_view(), name='logout'),
path('signup/',views.CreateUserView.as_view(),name='signup'),
url(r'loggedin', views.IndexView.as_view(),name = "loggedin")
]