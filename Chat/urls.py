from django.conf.urls import url, include
from django.contrib import admin
from chatapp import urls as urlschat

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^urlschat', include(urlschat))
]
