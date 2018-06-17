from django.urls import path
from django.conf.urls import include

from . import views


urlpatterns = [
    path('senddata/', views.senddata, name='senddata'),
    path('getdata/', views.getdata, name='getdata'),
]
handler404 = 'honoradar.views.handler404'
handler500 = 'honoradar.views.handler500'

#Add URL maps to redirect the base URL to our application
from django.views.generic import RedirectView
urlpatterns += [
    path('', RedirectView.as_view(url='/honoradar/', permanent=True)),
]
