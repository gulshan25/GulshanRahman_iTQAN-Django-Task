from django.db import models
from django.utils import timezone

# Create your models here.

class Category(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField('Category Name',max_length=100)
    
    def __str__(self):
        return self.name
  
class Product(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField('Product Name',max_length=100)
    price = models.DecimalField('Product Price',max_digits = 8,decimal_places=2,blank=True,null=True)
    photo = models.FileField(upload_to = "productimage",default = "productimage/blank.png",blank=True)
    category = models.ForeignKey('Category',on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name
     
    def get_absolute_url(self):
        return "/"