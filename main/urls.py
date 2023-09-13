from django.urls import path , include
from .views import *

app_name = 'main'


urlpatterns = [
    path("" , HomePageView.as_view() , name = "home"),
    path("region/<int:pk>" , RegionDetailView.as_view() , name = "region_detail"),
    path("region" , RegionView.as_view() , name ="region"),
    path("history_place" , HistoryPlaceView.as_view() , name= "history_place"),
    path("history_detail/<int:pk>/<int:kp>" , HistoryPlaceDetailView.as_view() , name ="history_detail"),
    path("attractions" , TopPlaceView.as_view() , name="attractions"),
    path("attraction_detail/<int:pk>/<int:pi>" , TopPlaceDetailView.as_view() , name="attraction_detail"),
    path("contact" , ContactView.as_view() , name="contact")
    
]