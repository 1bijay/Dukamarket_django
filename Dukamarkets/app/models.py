from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.

class Slider(models.Model):
    DISCOUNT_DEAL=(
        ('HOT DEALS','HOT DEALS'),
        ('New Arrivals','New Arrivals'),
        ('New Deals','New Deals'),
    )
    Image=models.ImageField(upload_to='media/slider_imgs')
    Discount_Deal=models.CharField(choices=DISCOUNT_DEAL, max_length=100)
    Sale=models.IntegerField()
    Brand_Name=models.CharField(max_length=200)
    Discount=models.IntegerField()
    link=models.CharField(max_length=200)

    #This code is written for showing objects name to real name in admin 
    def __str__(self):
        return self.Brand_Name  
    
class Banner_area(models.Model):
    image=models.ImageField(upload_to='media/banner_imgs')
    Discount_Deal=models.CharField(max_length=100)
    Quote=models.CharField(max_length=150)
    Discount=models.IntegerField()
    link=models.CharField(max_length=200,null=True)

    def __str__(self):
        return self.Quote 


class Main_Category(models.Model):
    name=models.CharField(max_length=100)
    def __str__(self):
        return self.name

class Category(models.Model):
    maincategory=models.ForeignKey(Main_Category,on_delete=models.CASCADE)
    name=models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
class Sub_Category(models.Model):
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    name=models.CharField(max_length=100)

    def __str__(self):
        return self.name
