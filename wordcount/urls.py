from django.conf.urls import url
from django.contrib import admin
from .views import hello
from .cps import count
from .cps import address
urlpatterns = [
    url(r'^address',address),
    url(r'^count',count),
    url(r'^admin/', admin.site.urls),
    url(r'^', hello),
]
