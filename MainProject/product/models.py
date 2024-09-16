from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=20)
    price = models.DecimalField(decimal_places=2,max_digits=10)

class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self) ->str:
        return self.name

# class category(models.Model):
#     name=models.CharField(max_length=25)  

class Product_type(models.Model):
    id=models.IntegerField(models.AutoField,primary_key=True,)
    name=models.CharField(max_length=25)
    description=models.TextField(verbose_name='desc')
    

  

