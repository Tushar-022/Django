
from django.urls import path
# Now import from current directory views file
from . import views  

#here we define all the routes
urlpatterns = [

    path('',views.all_chai,name="all_home"),

]