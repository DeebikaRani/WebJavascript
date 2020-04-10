from django.contrib import admin
from django.urls import path,include
from  pen import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path("",views.care,name='care')
]
