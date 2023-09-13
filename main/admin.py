from django.contrib import admin
from .models import *



@admin.register(Region)
class RegionAdmin(admin.ModelAdmin):
    search_fields = ['name']
    list_filter = ['name']

@admin.register(RegionDetail)
class RegionDetailAdmin(admin.ModelAdmin):
    search_fields = ['region']
    list_filter = ['region']

@admin.register(RegionDetailPhotoGallery)
class RegionDetailPhotoGalleryAdmin(admin.ModelAdmin):
    search_fields = ['region']
    list_filter = ['region']

@admin.register(RegionDetailClimate)
class RegionDetailClimateAdmin(admin.ModelAdmin):
    search_fields = ['region']
    list_filter = ['region']

@admin.register(RegionDetailGift)
class RegionDetailGiftAdmin(admin.ModelAdmin):
    search_fields = ['region']
    list_filter = ['region']

admin.site.register(RegionDetailGiftImage)
admin.site.register(RegionDetailFoodPhoto)


@admin.register(RegionDetailFood)
class RegionDetailFoodAdmin(admin.ModelAdmin):
    search_fields = ['region']
    list_filter = ['region']

@admin.register(RegionDetailPhotoZone)
class RegionDetailPhotoZoneAdmin(admin.ModelAdmin):
    search_fields = ['region']
    list_filter = ['region']

@admin.register(RegionDetailHistory)
class RegionDetailHistoryAdmin(admin.ModelAdmin):
    search_fields = ['region']
    list_filter = ['region']

@admin.register(HistoryPlaceDetail)
class HistoryPlaceDetailAdmin(admin.ModelAdmin):
    search_fields = ['name']
    list_filter = ['name']

@admin.register(TopPalace)
class TopPalaceAdmin(admin.ModelAdmin):
    search_fields = ['region']
    list_filter = ['region']

