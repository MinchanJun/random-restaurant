from django.conf.urls import url
from django.contrib.auth import views as auth_views
from . import views

app_name = 'randomshow'

urlpatterns =[
    url(r'^$',views.RandomshowList.as_view(),name='randomshow'),
    #url(r'^$',views.RandomeshowList.as_view(),name='all'),
]
