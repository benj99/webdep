from django.urls import path
from webapp import views


app_name = 'webapp'

urlpatterns = [
    path('',views.homepage,name='homepage'),
    path('pic1/',views.pic1,name='pic1'),
    path('pic2/',views.pic2,name='pic2'),
    path('pic3/',views.pic3,name='pic3'),
]
