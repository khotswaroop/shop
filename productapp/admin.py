from django.contrib import admin
from productapp.models import Product,UserModel,UserProfile,Recommendation
# Register your models here.

admin.site.register(Product)
admin.site.register(UserModel)
admin.site.register(UserProfile)
admin.site.register(Recommendation)
