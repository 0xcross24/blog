<<<<<<< HEAD
from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^$', views.articles_list),

]
=======
from django.conf.urls import include, url
from . import views

urlpatterns = [
	url(r'^$', views.article_list),
]
>>>>>>> 7e88efda4da329363e4b3c4565a61ee381ba6e4d
