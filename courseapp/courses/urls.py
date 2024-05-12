from django.urls import path
from . import views


#http://127.0.0.1:8000/client => anasayfa
#http://127.0.0.1:8000/client/home => anasayfa
#http://127.0.0.1:8000/client/kurslar => kurs listesi


urlpatterns = [
    path('', views.index),
    path('<category_name>', views.details),
    path('kategori/<int:category_id>',views.getCoursesByCategoryId),
    path('kategori/<str:category_name>', views.getCoursesByCategoryName, name='courses_by_category'),
    path('kategori/<str:category_text>',views.getCoursesByCategory),]