from django.db import models

# Create your models here.
class category(models.Model):
    category_img = models.FileField(upload_to="category_images/",max_length=250,null=True,default=None)
    category_title = models.CharField(max_length=50)

