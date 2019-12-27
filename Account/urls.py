
from django.contrib import admin
from django.urls import path,include
from .views import registerV,logoutV,loginV,updateV,passwordChangeV

app_name='Account'

urlpatterns = [

    path('register/',registerV,name='register'),
    path('update/',updateV,name='update'),
   # path('delete/<int:id>',deleteV,name='delete'),
    path('login/',loginV,name='login'),
    path('logout/',logoutV,name='logout'),
    path('password_change/',passwordChangeV,name='password_change'),

   # path('userlist/',userlistV,name='userlist'),
]
