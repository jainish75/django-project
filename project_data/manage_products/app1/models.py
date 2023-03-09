from django.db import models

# Create your models here.
class Company_data(models.Model):
    com_name = models.CharField(default="",max_length=200)
    com_em = models.EmailField(default="",max_length=200)
    com_cno =models.PositiveIntegerField(default=0)
    com_add = models.TextField(default="")
    join_date = models.DateField(auto_now=True,null=True,blank=True)
    profile = models.ImageField( upload_to="Comp_profile/", default="", max_length=300,null=True,blank=True)
    com_pass = models.CharField(default="",max_length=300)

def __str__(self) ->str:
    return self.com_name
    