from django.conf.urls import include,url
from  django.contrib import admin
from contactform1app import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$',views.Contact_view)
]
