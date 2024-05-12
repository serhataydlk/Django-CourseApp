from django.contrib import admin
from django.http import HttpResponse
from django.shortcuts import render
from django.urls import path,include

def home(request):
    return render(request,'index.html')

def kurslar(request):
    return HttpResponse('kurs listesi')

def hakkimizda(request):
    return HttpResponse('hakkımızda sayfası')   

def iletisim(request):
    return HttpResponse('iletişim sayfası')

urlpatterns = [
    path('',include('pages.urls')),  
    path('kurslar/',include('courses.urls')),  
    path('admin/', admin.site.urls),
]

#coursesapp
#courses
#pages linkleri karşılamak için oluşturuldu

