
from django.contrib import admin
from django.urls import path,include
from .views import createV,deleteV,updateV,sentpostV,inboxpostV,pendingpostV,refusedpostV,confirmedpostV,adminconfirmedpostV,adminrefusedpostV,adminpendingpostV

app_name='Post'

urlpatterns = [

    path('create/',createV,name='create'),
    path('delete/<int:id>',deleteV,name='delete'),
    path('update/<int:id>',updateV,name='update'),
    path('sent/',sentpostV.as_view(),name='sent'),
    path('inbox/',inboxpostV.as_view(),name='inbox'),

    path('pending/',pendingpostV.as_view(),name='pending'),
    path('pending_all/',adminpendingpostV.as_view(),name='pending_all'),

    path('refused/',refusedpostV.as_view(),name='refused'),
    path('refused_all/',adminrefusedpostV.as_view(),name='refused_all'),

    path('confirmed/',confirmedpostV.as_view(),name='confirmed'),
    path('confirmed_all/',adminconfirmedpostV.as_view(),name='confirmed_all'),
    
]
