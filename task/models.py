from django.db import models

# Create your models here.
class Profile(models.Model):
    name =models.CharField(max_length=200,null=True,blank=True)
    image_i = models.ImageField(null=True,blank=True)
    resume = models.FileField(null=True, blank=True)
    

    def __str__(self):
        return self.name

        

class Projects(models.Model):
    name =models.CharField(max_length=200,null=True,blank=True)
    short_description =models.CharField(max_length=255,null=True,blank=True)
    description =models.TextField(null=True,blank=True)
    image = models.ImageField(null=True,blank=True)

    def __str__(self):
        return self.name