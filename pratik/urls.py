from django.urls import path
from pratik import views
from .views import  GeneratePdf_Resume 

urlpatterns = [
    path('' , views.index , name="index"),
    path('save/' , views.saveView , name="save") ,
    path("resume/pdf" , GeneratePdf_Resume.as_view() , name="resume/pdf") ,
]
