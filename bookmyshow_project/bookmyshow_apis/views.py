from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Cinemas_table,users_table
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import View
from django.shortcuts import redirect

from rest_framework import permissions
from rest_framework.generics import CreateAPIView
from django.contrib.auth import get_user_model # If used custom user model
from rest_framework.decorators import api_view, renderer_classes
from rest_framework.renderers import JSONRenderer, TemplateHTMLRenderer
from .serializers import UserSerializer

from django.views.generic import TemplateView


class list_all_movies_per_city(APIView ):

  def get(self, request):
    city_name  = request.data["city"]
    print(city_name)
    query_result = Cinemas_table.objects.filter(theatre_city=city_name).values('movie_name')
    print(query_result)
    result_list= []
    for rst in query_result:
    	result_list.append(rst["movie_name"])

    result_list  = list(set(result_list))
    print(query_result)

    return Response({"results":result_list})

class cinema_theatres_with_show_timings(APIView ):

  def get(self, request):
    movie_name  = request.data["movie_name"]
    print(movie_name)
    query_result = Cinemas_table.objects.filter(movie_name=movie_name).values('movie_name','theatre_name','theatre_timings','theatre_city')
    print(query_result)
    result_list= []
    for rst in query_result:
      result_list.append([rst["movie_name"],rst['theatre_name'],rst['theatre_timings'],rst['theatre_city']])

    # result_list  = list(set(result_list))
    print(query_result)

    return Response({"results":result_list})


class showtime_seats_availability(APIView ):

  def get(self, request):
    movie_name  = request.data["movie_name"]
    theatre_name  = request.data['theatre_name']
    theatre_city = request.data['theatre_city']
    # print(movie_name)
    query_result = Cinemas_table.objects.filter(movie_name=movie_name,theatre_name=theatre_name,theatre_city=theatre_city).values('movie_name','theatre_name','theatre_timings','theatre_show_timing_total_seats','theatre_show_timings_current_seats','theatre_city')
    # print(query_result)
    result_list= []
    for rst in query_result:
      if rst['theatre_show_timings_current_seats']<rst['theatre_show_timing_total_seats']:
        result_list.append([rst["movie_name"],rst['theatre_name'],rst['theatre_timings'],rst['theatre_city'],"Available"])
      else:
        result_list.append([rst["movie_name"],rst['theatre_name'],rst['theatre_timings'],rst['theatre_city'],"Not Available"])

    # result_list  = list(set(result_list))
    # print(query_result)

    return Response({"results":result_list})


@api_view(['GET'])
@login_required
def booktickets(request):
    if not request.user.is_authenticated:
        return redirect('login')
    else:
        return Response({"results":"ticket_booked"})

class CreateUserView(CreateAPIView):

    model = get_user_model()
    permission_classes = [
        permissions.AllowAny # Or anon users can't register
    ]
    serializer_class = UserSerializer

class IndexView(TemplateView):
  template_name = "index.html"