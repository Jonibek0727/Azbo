from datetime import datetime
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User, AbstractUser


class CostomUser(AbstractUser):
    is_admin = models.BooleanField(default=False, null=True)
    is_operator = models.BooleanField(default=False, null=True)
    is_shop = models.BooleanField(default=False, null=True)
    is_shop_child = models.BooleanField(default=False, null=True)
    parent = models.CharField(max_length=255, null=True)

   



# Create your models here.
class Department(models.Model):
    user = models.ForeignKey(CostomUser, on_delete=models.CASCADE, null=True)
    name = models.TextField(null=True) 
    Tel_derector = models.CharField(max_length=13,null=True)
    Tel_bugalter = models.CharField(max_length=13,null=True)
    Inn = models.IntegerField(null=True)
    Xisob_raqam = models.IntegerField(null=True)
    gvohnoma = models.FileField(upload_to='photo/Guvohnoma/',null=True, blank=True)
    Derector_pasporti = models.FileField(upload_to='photo/Derector_pasport/',null=True, blank=True)
    Adresss = models.TextField(null=True)
    foiz_narx = models.IntegerField(null=True)
    status = models.IntegerField(null=True) 
    creater = models.CharField(max_length=255, null=True)
    date_added = models.DateTimeField(default=timezone.now, null=True) 
    date_updated = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return self.name

class Muddat(models.Model):
    muddat = models.IntegerField()

    def __str__(self) :
        return str(self.muddat)

status = (
    ('Новый', "Новый " ),
    ('Рассматривается', "Рассматривается" ),
    ('Qaytish', 'Qaytish'),
    ('SMS', 'SMS'),
    ('SMS_send', 'SMS_send'),
    ('Одобрено', "Одобрено " ),
    ('Отказано' , "Отказано " ),
    ('Karta', 'Karta'),
    ('Оформлено' , "Оформлено " ),
    ('Shartnoma' , "Shartnoma " ),
    ('ok' , "ok " ),
    ('Отменено' , "Отменено  " ),
)

class Arizalar(models.Model):
    parent = models.ForeignKey(Department, on_delete=models.CASCADE, null=True, blank=True)
    first_name = models.CharField(max_length=255, null=True, blank=True)
    last_name = models.CharField(max_length=255, null=True, blank=True)
    tel = models.CharField(max_length=255, null=True, blank=True)
    status = models.CharField(max_length=50, choices=status, default="Новый", null=True, blank=True)
    date_added = models.DateTimeField(auto_now=True, null=True, blank=True) 
    type_muddat = models.ForeignKey(Muddat, on_delete=models.CASCADE, null=True, blank=True)
    pasport_seria = models.CharField(max_length=10, null=True, blank=True)
    data_user =  models.DateField(blank=True,null= True) 
    pasport_photo = models.FileField(upload_to='photo/pasport',  null=True, blank=True)
    code_pasport = models.CharField(max_length=255, null=True, blank=True)
    commet = models.TextField(null=True, blank=True)
    summa_limet = models.CharField(max_length=255, null=True, blank=True)
    maxshulot_summasi = models.CharField(max_length=255, null=True, blank=True)
    yechiladigon_summa = models.CharField(max_length=255, null=True, blank=True)
    oylik_tolov = models.CharField(max_length=255, null=True, blank=True)
    shartnoma_asli1 = models.FileField(upload_to='photo/Shartnoma_asli1', null=True, blank=True)
    shartnoma_asli2 = models.FileField(upload_to='photo/Shartnoma_asli2', null=True, blank=True)
    selfe_photo = models.FileField(upload_to='photo/selfi', null=True, blank=True)
    shantnoma_imzo1 = models.FileField(upload_to='photo/shantnoma_imzo1', null=True, blank=True)
    shantnoma_imzo2 = models.FileField(upload_to='photo/shantnoma_imzo2', null=True, blank=True)
    chek_photo = models.FileField(upload_to='photo/shantnoma_imzo', null=True, blank=True)
    operator = models.CharField(max_length=255, null=True, blank=True)


    def __str__(self):
        return self.first_name















class Position(models.Model):
    name = models.TextField() 
    description = models.TextField() 
    status = models.IntegerField() 
    date_added = models.DateTimeField(default=timezone.now) 
    date_updated = models.DateTimeField(auto_now=True) 

    def __str__(self):
        return self.name


class Employees(models.Model):
    code = models.CharField(max_length=100,blank=True) 
    firstname = models.TextField() 
    middlename = models.TextField(blank=True,null= True) 
    lastname = models.TextField() 
    gender = models.TextField(blank=True,null= True) 
    dob = models.DateField(blank=True,null= True) 
    contact = models.TextField() 
    address = models.TextField() 
    email = models.TextField() 
    department_id = models.ForeignKey(Department, on_delete=models.CASCADE) 
    position_id = models.ForeignKey(Position, on_delete=models.CASCADE) 
    date_hired = models.DateField() 
    salary = models.FloatField(default=0) 
    status = models.IntegerField() 
    date_added = models.DateTimeField(default=timezone.now) 
    date_updated = models.DateTimeField(auto_now=True) 

    def __str__(self):
        return self.firstname + ' ' +self.middlename + ' '+self.lastname + ' '
