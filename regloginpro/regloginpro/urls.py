from django.conf.urls import url
from django.contrib import admin
from regloginapp import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'$',views .reg_view),
    url(r'^$',views.login_view),
    url(r'^login',views.login_view),
]
