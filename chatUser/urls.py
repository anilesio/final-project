from django.contrib import admin
from django.urls import path
from django.conf.urls import include,url
from django.conf.urls.static import static
from .views import *

urlpatterns = [
    # url(r'^$',index, name="index" ),

    url(r'chat-user/$', chatUser, name='chat-user'),

]
