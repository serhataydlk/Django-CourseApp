from datetime import date,datetime
from django.shortcuts import redirect,render
from django.http import HttpResponse,HttpResponseNotFound
from django.urls import reverse
# Create your views here.




# http://127.0.0.1:8000/kurslar

data = {
    "programlama":"Programlama Kategorisine Ait Kurslar",
    "web-geliştirme":"Web-Geliştirme Kategorisine Ait Kurslar",
    "mobil-uygulamalar":"Mobil Geliştirme Kategorisine Ait Kurslar",
}
db = {   
    "courses":[
        {
            "title":"Javascript Kursu",
            "description":"Javascript Kurs Açıklaması",
            "imageUrl":"1.jpeg",
            "slug":"javascript-kursu",
            "date":datetime.now(),
            "isActive": True,
            "isUpdated": False
        },
        {
            "title":"Python Kursu",
            "description":"Python Kurs Açıklaması",
            "imageUrl":"2.jpeg",
            "slug":"python-kursu",
            "date": datetime.now(),
            "isActive":False,
            "isUpdated":True,
            
        },
        {
            "title":"Web Geliştirme Kursu",
            "description":" Web Geliştirme Kurs Açıklaması",
            "imageUrl":"3.jpeg",
            "slug":"web-gelistirme-kursu",
            "date": date(2024,3,30),
            "isActive": True,  
            "isUpdated": True,
        }
    ],
    "categories":[
        {"id":1,"name":"Programlama", "slug":"programlama"},
        {"id":2,"name":"Web Geliştirme", "slug":"web-geliştirme"},
        {"id":3,"name":"Mobil Uygulamalar", "slug":"mobil-uygulamalar"},    
    ] 
}




def index(request):
    kurslar = [course for course in db["courses"] if course  ["isActive"]==True]
    kategoriler = db["categories"]

    for kurs in db["courses"]:
        if kurs["isActive"] == True:
            kurslar.append(kurs)
    
    return render(request,'courses/index.html',{
            'categories': kategoriler,
            'courses': db["courses"]
    })
    

    
    

def details(request ,category_name):
    try:
        category_text = data[category_name];
        return render(request, 'courses/kurslar.html', {

            'category':category_name,
            'category_text': category_text

        })
            
    except:
        return HttpResponseNotFound("<h1>yanlış kategori seçimi</h1>")
    
    
    

    
        # return HttpResponse(f"{kurs_adi}")


def getCoursesByCategoryName(request,category_name):
    # return HttpResponseNotFound(data)
    try:
        category_text = data[category_name];
        return render(request, 'courses/kurslar.html', {

            'category':category_name,
            'category_text': category_text
                 

        })
            
    except:
        return HttpResponseNotFound("<h1>yanlış kategori seçimiiiiii</h1>")
    

def getCoursesByCategory(request,category_name):
    text = ""

    if (category_name == "programlama"):
        text = "programlama kategorisine ait kurslar"
    elif (category_name == "web-gelistirme"):
        text = "web geliştirme kategorisine ait kurslar"
    elif(category_name == "mobil"):
        text = "mobil kategorisine ait kurslar"
    elif(category_name == "C#"):
        text = "C# Kategorisine ait kurslar"
    else:
        text = "yanlış kategori seçimi"

    return HttpResponse(text)


def getCoursesByCategoryId(request,category_id):
   category_list = list(data.keys())
   if category_id>len(category_list):
       return HttpResponseNotFound("<h1>Yanlış Kategori Seçimiiiiiii</h1>")
   redirect_text = category_list[category_id -1]
   return redirect('/kurslar/kategori/'+ redirect_text) 