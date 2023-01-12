from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django import include

urlpatterns = [
    path('',views.home, name ='home'),
    path('accounts/',include('accounts.url'))

]

urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)