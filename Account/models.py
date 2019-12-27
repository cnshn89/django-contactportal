from django.db import models
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager
# Create your models here.


class ProjectAccountManager(BaseUserManager):
    def create_user(self,email,username,password=None):
        if not email:
            raise ValueError ("Email adresi alanı boş olamaz")
        if not username:
            raise ValueError ("Kullanıcı adı alanı boş olamaz")   

        user=self.model(
            email=self.normalize_email(email),
            username=username,
            
        ) 
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self,email,username,password=None):
 
        user=self.create_user(
            email=self.normalize_email(email),
            username=username,
            password=password,
            
        ) 
        user.is_admin=True
        user.is_staff=True
        user.is_superuser=True
        user.save(using=self._db)
        return user

class Account(AbstractBaseUser):

    DEPARTMENT ={
        ('U','Üretim'),
        ('P','Pazarlama'),
        ('S','Satın Alma'),
        ('A','ARGE'),
        ('M','Muhasebe'),
        ('F','Finans'),
    }
    email = models.EmailField(verbose_name="Email",max_length=60,unique=True)
    username = models.CharField(max_length=30,unique=True,verbose_name= "Kullanıcı Adı")
    first_last_name=models.CharField(max_length=60,verbose_name= "Ad Soyad")
    department=models.CharField(max_length=1,verbose_name="Departman",choices=DEPARTMENT)
    date_joined=models.DateTimeField(verbose_name="Kayıt Tarihi",auto_now_add=True)
    last_login=models.DateTimeField(verbose_name="Son Giriş Tarihi",auto_now=True)
    is_admin=models.BooleanField(default=False,verbose_name="Admin mi ?")
    is_active=models.BooleanField(default=True,verbose_name="Aktif mi ?")
    is_staff=models.BooleanField(default=False,verbose_name="Yetkili mi ?")
    is_superadmin=models.BooleanField(default=False,verbose_name="Super Admin mi ?")
    
    USERNAME_FIELD='email'
  
    objects=ProjectAccountManager()

    def __str__(self):
        return self.first_last_name

    def has_perm(self,perm,obj=None):
        return self.is_admin
    
    def has_module_perms(self,app_label):
        return True

