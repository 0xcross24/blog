"""blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
<<<<<<< HEAD
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
=======
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
>>>>>>> 7e88efda4da329363e4b3c4565a61ee381ba6e4d
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
<<<<<<< HEAD
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
=======
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
>>>>>>> 7e88efda4da329363e4b3c4565a61ee381ba6e4d
from django.contrib import admin
from . import views

urlpatterns = [
<<<<<<< HEAD
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.home),
    url(r'^about/$', views.about),
    url(r'^articles/', include('articles.urls')),
=======
    url(r'^admin/', include(admin.site.urls)),
    url(r'^about/$', views.about),
    url(r'^articles/', include('articles.urls')),
    url(r'^$', views.home),
>>>>>>> 7e88efda4da329363e4b3c4565a61ee381ba6e4d

]
