from django.contrib import admin
from groceryproducts.models import category


# Register your models here.
class categoryAdmin(admin.ModelAdmin):
    list_display = ('category_img','category_title')
    
admin.site.register(category,categoryAdmin)  