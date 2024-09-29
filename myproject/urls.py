"""
URL configuration for myproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from myapp.views import current_date_time,four_hours_ahead, four_hours_before
from myapp2.views import showlist, home, aboutus,contactus
urlpatterns = [
    path('admin/', admin.site.urls),
    path('cdt/', current_date_time),
    path('fha/', four_hours_ahead),
    path('fhb/', four_hours_before),
    path('showlist/', showlist),
    path('home/', home),
    path('aboutus/', aboutus),
    path('contactus/', contactus),
    
]
