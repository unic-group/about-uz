from django.db import models

# Create your models here.


class Region(models.Model):
    name = models.CharField(verbose_name = "Viloyat nomi (uz): " , max_length=150)
    image_region = models.ImageField(verbose_name = "Viloyat asosiy rasmi: ", upload_to="region_photo")
    teg = models.CharField(verbose_name="Viloyat tegi (uz): " , max_length=150)
    reg_date = models.DateField(auto_now_add=True)

    def __str__(self) -> str:
        return self.name
    

    class Meta:
        verbose_name = "Viloyat"
        verbose_name_plural = "Viloyatlar"


class RegionDetail(models.Model):
    region = models.ForeignKey(Region , verbose_name ="Viloyatni tanlang: " , on_delete=models.PROTECT)
    decription = models.TextField(verbose_name = "Viloyat haqida: ")
    image_header = models.ImageField(verbose_name = "Viloyat header rasmi: " , upload_to ="image_header")
    image = models.ImageField(verbose_name="viloyat rasmi: " , upload_to="region_photo")
    map = models.TextField(verbose_name = "Vioyat xaritasi: ")
    
    def __str__(self) -> str:
        return f"{self.region}"
    

    class Meta:
        verbose_name = "Viloyat malumoti"
        verbose_name_plural = "Viloyatlar malumoti"

class RegionDetailPhotoGallery(models.Model):
    region = models.ForeignKey(Region , verbose_name ="Viloyatni tanlang: " , on_delete=models.PROTECT)
    image = models.ImageField(verbose_name="Viloyat Rasmi: " , upload_to="photogallery")
    
    def __str__(self) -> str:
        return f"{self.region}"
    
class RegionDetailClimate(models.Model):
    region = models.ForeignKey(Region , verbose_name ="Viloyatni tanlang: " , on_delete=models.PROTECT)
    title = models.TextField(verbose_name="Iqlim haqida: ")
  

    def __str__(self) -> str:
        return f"{self.region}"
    
class RegionDetailGift(models.Model):
    region = models.ForeignKey(Region , verbose_name='Viloyatni tanlang: ' , on_delete=models.PROTECT)
    description = models.TextField(verbose_name="Sovga va suvinerlar haqida: ")


    def __str__(self) -> str:
        return f"{self.region}"
    
class RegionDetailGiftImage(models.Model):
    gift = models.ForeignKey(Region , verbose_name='sovga va suvinerlar : ' , on_delete=models.PROTECT)
    image = models.ImageField(verbose_name = "Sovga va suvinerlar rasmi: " , upload_to = "gift_photo")


    def __str__(self) -> str:
        return f"{self.gift}"
    
class RegionDetailFood(models.Model):
    region = models.ForeignKey(Region , verbose_name="Viloyatni tanlang: " , on_delete=models.PROTECT)
    description = models.TextField(verbose_name="Viloyat milliy taomlari haqida : " )
    
    def __str__(self) -> str:
        return f"{self.region}"
    
class RegionDetailFoodPhoto(models.Model):
    food = models.ForeignKey(Region , verbose_name = "Viloyatni tanlang: " , on_delete=models.PROTECT)
    image = models.ImageField(verbose_name="Milliy taomlar: " , upload_to="food_photo")


    def __str__(self) -> str:
        return f"{self.food }"
    
class RegionDetailPhotoZone(models.Model):
    region = models.ForeignKey(Region , verbose_name="Viloyatni tanlang: " , on_delete=models.PROTECT)
    description = models.TextField(verbose_name="Fotozona lar haqida: ")
    map = models.TextField(verbose_name="Fotozonalar xaritasi: ")
    image = models.ImageField(verbose_name="Fotozona rasmi: " , upload_to="photo_zone_image")


    def __str__(self) -> str:
        return f"{self.region}"
    
class RegionDetailHistory(models.Model):
    region = models.ForeignKey(Region , verbose_name="Viloyatni tanlang: " , on_delete=models.PROTECT)
    description = models.TextField(verbose_name="Viloyat tarixi haqida: " )
    image = models.ImageField(verbose_name="Viloyat tarixi rasmi: " , upload_to="history_photo")


    def __str__(self) -> str:
        return f"{self.region}"
    




class HistoryPlaceDetail(models.Model):
    region = models.ForeignKey(Region , verbose_name ='Viloyatni tanlang: ' , on_delete=models.PROTECT)

    name = models.CharField(verbose_name = "tarixiy joy nomi: " , max_length=150)

    image_header = models.ImageField(verbose_name="Header rasmi: " , upload_to="header_photo")
    title1 = models.TextField("tarixiy joy haqida (1): ")
    image1 = models.ImageField(verbose_name="Tarixiy joy rasmi: " , upload_to="histoy_place_photo")
    image1_1 = models.ImageField(verbose_name="Tarixiy joy rasmi: " , upload_to="histoy_place_photo")
    

    title2 = models.TextField("tarixiy joy haqida (2): ")
    image2 = models.ImageField(verbose_name="Tarixiy joy rasmi: " , upload_to="histoy_place_photo")
    title3 = models.TextField(verbose_name="Tarixiy joy haqida (3): ")
    image3 = models.ImageField(verbose_name="tarixiy joy rasmi (3): ")
    map = models.TextField(verbose_name="Joylashuv qismi karta: " )

    
    def __str__(self) -> str:
        return f"{self.region}"
    



class TopPalace(models.Model):
    region = models.ForeignKey(Region , verbose_name="Viloyatni tanlang: " , on_delete=models.PROTECT)
    name = models.CharField(verbose_name="Diqqatga sazovor joy nomi: " , max_length=150)
    image_header = models.ImageField(verbose_name="Diqqatga sazovor joylar header rasmi: " , upload_to="attractions_photo_header")
    image1 = models.ImageField(verbose_name="Diqqatga sazovor joylar rasmi (1): " , upload_to="attracions_photo1")
    image2 = models.ImageField(verbose_name="Diqqatga sazovor joylar rasmi (2): " , upload_to="attracions_photo2")
    image3 = models.ImageField(verbose_name="Diqqatga sazovor joylar rasmi (3): " , upload_to="attracions_photo3")
    image4 = models.ImageField(verbose_name="Diqqatga sazovor joylar rasmi (4): " , upload_to="attracions_photo4")
    title1 = models.TextField(verbose_name="Diqqatga sazovor joylar haqida (1): " )
    title2 = models.TextField(verbose_name="Diqqatga sazovor joylar haqida (2): " )
    title3 = models.TextField(verbose_name="Diqqatga sazovor joylar haqida (3): " )
    map = models.TextField(verbose_name="Diqqatga sazovor joylar manzili: ")

    def __str__(self) -> str:
        return f"{self.region}"

    


class Contact(models.Model):
    name = models.CharField(verbose_name="Mijoz ismi: " , max_length=150)
    email = models.CharField(verbose_name="Mijoz email pochtasi: " , max_length=150)
    description = models.TextField(verbose_name="Mijoz matni: " )    

    def __str__(self) -> str:
        return self.name