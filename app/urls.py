
from django.urls import path 
from . import views
urlpatterns = [
    
    path('' , views.app , name = 'app'), 
    path('<int:app_id>/' , views.app_description, name= 'app_description') , 

]