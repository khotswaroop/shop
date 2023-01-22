from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Product(models.Model):
    id=models.IntegerField(primary_key=True)
    shape=models.CharField(max_length=20)
    size=models.IntegerField()
    location=models.CharField(max_length=20)
    price=models.IntegerField()
    def __str__(self):
        return self.shape

class UserModel(models.Model):
    id=models.IntegerField(primary_key=True)
    name=models.CharField(max_length=20)
    age=models.IntegerField()
    address=models.CharField(max_length=20)
    def __str__(self):
        return self.name

class UserProfile(models.Model):
    id=models.IntegerField(primary_key=True)
    name=models.OneToOneField(User,on_delete=models.CASCADE)
    age=models.IntegerField()
    address=models.CharField(max_length=20)
    class Meta:
        db_table='productuser'
    def __str__(self):
        return self.name

class Recommendation(models.Model):
    product=models.OneToOneField(Product,on_delete=models.CASCADE)
    user=models.OneToOneField(UserModel,on_delete=models.CASCADE)
    def __str__(self):
        return str(self.product)

