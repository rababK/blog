"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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


from django.urls import include, path
from django.contrib.admin import AdminSite
from django.contrib import admin
from django.conf.urls import url, include

admin.autodiscover()



urlpatterns = [

    path('',  include('blog.urls')),
    url('admin/', admin.site.urls),
    ]



    #url(r'^$', views.home, name='home'),
    #path('acounts/', include('django.contrib.auth.urls')),
    #url(r'^ Afterlog/$', views.Afterlog, name='Afterlog'),
    #url(r'^ logout/$', views.logout, name='logout'),



