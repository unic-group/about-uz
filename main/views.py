from django.shortcuts import render, redirect
from django.views import View
from .models import *
import random
from .tools import *

class HomePageView(View):
    def get(self , request):
        region = Region.objects.all()
        region2 = Region.objects.all()[:6]
        history_place_all = HistoryPlaceDetail.objects.all()
        top_place = TopPalace.objects.all()
  
        random_numbers = set()

        while len(random_numbers) < 10:
            random_numbers.add(random.randint(0, 20))

        for i in random_numbers:
            history_place_all1 = HistoryPlaceDetail.objects.filter(id=i)
            context = {
            "region":region,
            "region2":region2,
            "history_all":history_place_all1,
            "history_place_all":history_place_all   ,
            "top_place":top_place
            }
            return render(request , "home.html" , context )
    
class RegionDetailView(View):
    def get(self,request , pk):
        region = Region.objects.all()
      


    
        region2 = Region.objects.get(id=pk)
        region3 = Region.objects.all()[:3]
        region_detail = RegionDetail.objects.get(region=region2)  
        photo_gallery = RegionDetailPhotoGallery.objects.filter(region=region2)
        climate = RegionDetailClimate.objects.get(region=region2)
        gift = RegionDetailGift.objects.get(region=region2)
        gift_photo = RegionDetailGiftImage.objects.filter(gift=region2)
        food = RegionDetailFood.objects.get(region=region2)
        food_photo = RegionDetailFoodPhoto.objects.filter(food=region2)
        photo_zone = RegionDetailPhotoZone.objects.filter(region=region2)
        history = RegionDetailHistory.objects.filter(region=region2)
        history_place = HistoryPlaceDetail.objects.filter(region=region2)
        history_place_all = HistoryPlaceDetail.objects.all()
        top_place = TopPalace.objects.all()
        random_numbers = set()

        while len(random_numbers) < 10:
            random_numbers.add(random.randint(0, 20))

        for i in random_numbers:
            history_place_all1 = HistoryPlaceDetail.objects.filter(id=i)
            context = {
            "region":region,
            "region2":region2,
            "region3":region3,
            "region_detail":region_detail,
            "photo_gallery":photo_gallery,
            "climate":climate,
            "gift":gift,
            "gift_photo":gift_photo,
            "food":food,
            "food_photo":food_photo,
            "photo_zone":photo_zone ,
            "history":history,
            "history_place":history_place ,   
            "history_all":history_place_all1,
            "history_place_all":history_place_all,
            "top_place":top_place
            }

            return render(request , "region_detail.html" , context)
class RegionView(View):
    def get(self , request):
        region = Region.objects.all()
        history_place_all = HistoryPlaceDetail.objects.all()
        top_place = TopPalace.objects.all()
  
        random_numbers = set()

        while len(random_numbers) < 10:
            random_numbers.add(random.randint(0, 20))

        for i in random_numbers:
            history_place_all1 = HistoryPlaceDetail.objects.filter(id=i)
            context = {
            "region":region,
            "history_all":history_place_all1,
            "history_place_all":history_place_all   ,
            "top_place":top_place
            }
            return render(request , "region.html" , context )
    
class HistoryPlaceDetailView(View):
    def get(self , request , pk , kp):
        region = Region.objects.all()
        region2 = Region.objects.get(id=pk)
        region3 = Region.objects.all()[:3]

        history_place = HistoryPlaceDetail.objects.get(id=kp)
        history_place_all = HistoryPlaceDetail.objects.all()
        history_place_region = HistoryPlaceDetail.objects.filter(region=region2)
        top_place = TopPalace.objects.all()
        random_numbers = set()

        while len(random_numbers) < 10:
            random_numbers.add(random.randint(0, 20))

        for i in random_numbers:
            history_all = HistoryPlaceDetail.objects.filter(id=i)
      
       
            context ={
            "region":region,
            "region2":region2,
            "region3":region3,
            "history_place":history_place,
            "history_all":history_all,
            "history_place_region":history_place_region,
            "top_place":top_place,
            "history_place_all":history_place_all
            }
            return render(request , "history_detail.html" ,context )
    


class HistoryPlaceView(View):
    def get(self, request):
        region = Region.objects.all()
        history_place_all = HistoryPlaceDetail.objects.all()
        top_place = TopPalace.objects.all()
  
        random_numbers = set()

        while len(random_numbers) < 10:
            random_numbers.add(random.randint(0, 20))

        for i in random_numbers:
            region2 = Region.objects.filter(id=i)
            history_all = HistoryPlaceDetail.objects.filter(id=i)
            context = {
            "region":region,
            "region2":region2,
            "history_place_all":history_place_all   ,
            "history_all":history_all,
            "top_place":top_place
            }
            return render(request , "history_place.html" , context)
        


class TopPlaceView(View):
    def get(self ,request):
        region = Region.objects.all()
        history_place_all = HistoryPlaceDetail.objects.all()
        top_place = TopPalace.objects.all()
  
        random_numbers = set()

        while len(random_numbers) < 10:
            random_numbers.add(random.randint(0, 20))

        for i in random_numbers:
            history_place_all1 = HistoryPlaceDetail.objects.filter(id=i)
            context = {
            "region":region,
            "history_all":history_place_all1,
            "history_place_all":history_place_all,  
            "top_place":top_place 
            }
            return render(request , "top_place.html" , context )

    
class TopPlaceDetailView(View):
    def get(self , request , pk , pi):
        region = Region.objects.all()
        region2 = Region.objects.get(id=pk)
        region3 = Region.objects.all()[:3]

        history_place_all = HistoryPlaceDetail.objects.filter(region=region2)
        top_place = TopPalace.objects.get(id=pi)
        top_place_all = TopPalace.objects.all()
  
        random_numbers = set()

        while len(random_numbers) < 10:
            random_numbers.add(random.randint(0, 20))

        for i in random_numbers:
            history_place_all1 = HistoryPlaceDetail.objects.filter(id=i)
            context = {
            "region":region,
            "region2":region2,
            "region3":region3,
            "history_all":history_place_all1,
            "history_place_all":history_place_all   ,
            "top_place":top_place,
            "top_place_all":top_place_all
            }
            return render(request , "top_place_detail.html" , context)
class ContactView(View):
    def get(self ,request):
        region = Region.objects.all()
        region2 = Region.objects.all()[:6]
        history_place_all = HistoryPlaceDetail.objects.all()
        top_place = TopPalace.objects.all()
  
        random_numbers = set()

        while len(random_numbers) < 10:
            random_numbers.add(random.randint(0, 20))

        for i in random_numbers:
            history_place_all1 = HistoryPlaceDetail.objects.filter(id=i)
            context = {
            "region":region,
            "region2":region2,
            "history_all":history_place_all1,
            "history_place_all":history_place_all   ,
            "top_place":top_place
            }
            return render(request , "contact.html" , context )
    def post(self , request):
        name = request.POST["name"]
        email = request.POST["email"]
        text = request.POST["text"]
        contect(email ,name)
        contact = Contact.objects.create(name = name , email=email , description=text)
        return redirect("main:home")