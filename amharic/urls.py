from django.urls import path,re_path
from . import views

app_name = 'amharic'
urlpatterns = [
    path("",views.index,name="amharic"),
    path("about/",views.about,name="a_about"),
    path("faq/",views.faq,name="a_faq"),
]