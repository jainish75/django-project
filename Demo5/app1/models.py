from django.db import models

# Create your models here.
class Table1(models.Model):
    emp_nm=models.CharField("Emploee Name",default='',blank=True,null=True,max_length=50)
    emp_id=models.PositiveIntegerField("Emploee Ids",default=0)
    emp_em=models.EmailField("Employee Email", default='',blank=True,null=True)
    emp_cno = models.IntegerField("Emploee Contact NO",default=0)
    emp_add1=models.TextField("Emploee Adress1",default="")
    emp_add2=models.TextField("Emploee Adress2",default="")

def __str__(self):
    return self.emp_nm
        
    