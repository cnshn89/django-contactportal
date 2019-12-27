from django.db import models
from django.conf import settings
from datetime import date
from django.utils.text import slugify
from unidecode import unidecode
from multiselectfield import MultiSelectField


STATUS = (
    ("0","Onay Bekliyor"),
    ("1","Onaylandı"),
    ("2","Reddedildi"),
    )   

SUBJECT = (
    ("U","Üretim İş Emri hk."),
    ("P","Planlama hk."),
    ("S","Satın Alma hk."),
    ("M","Müşteri Siparişi hk."),
    ("D","Diğer"),
    )     


MAIL_GROUP = (
    ("Y","Üst Yönetim"),
    ("F","Finansman"),
    ("S","Ticari Satın Alma"),
    ("M","Muhasebe"),
    ("IP","Yurtiçi Satış"),
    ("IH","İhracat Satış"),
    ("P","Planlama"),
    ("U","Üretim"),
    ("D","Depo"),
    ("B","Bilgi İşlem"),
    ("E","E-Ticaret"),
    ("IK","İnsan Kaynakları"),
    ("G","Genel"),
    )   





class Post(models.Model):
    title = models.CharField(max_length=200,verbose_name="Başlık")
    # slug = models.SlugField(max_length=200, unique=True,blank=True)
    subject=models.CharField(max_length=1,verbose_name="Konu",choices=SUBJECT)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete= models.CASCADE)
    updated_on = models.DateTimeField(auto_now= True)
    content = models.TextField(verbose_name="İçerik")
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=2,verbose_name="Mesaj Durumu",choices=STATUS,default="0")
    mail_group=MultiSelectField(verbose_name="Mail Grupları",choices=MAIL_GROUP,blank=True,null=True)
    docnumber=models.CharField(max_length=200,verbose_name="Belge No",blank=True,null=True)
    duedate=models.DateField(verbose_name="Termin Tarihi",blank=True,null=True)

    class Meta:
        ordering = ['-created_on']
        #unique_together = ("title", "slug")

    def __str__(self):
        return self.title

    # def save(self, *args, **kwargs):
    #     self.slug = slugify(unidecode(self.title))
    #     super(Post, self).save(*args, **kwargs)