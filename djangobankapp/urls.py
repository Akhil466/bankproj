from django.urls import  path
from djangobankproj import settings
from django . conf . urls.static import static

from . import views
app_name='djangobankapp'
urlpatterns = [
    path('',views.home,name='home'),
    path('register',views.register,name='register'),
    path('login', views.login, name='login'),
    path('app',views.app,name='app'),


    path('ajax/load-cities/', views.load_cities, name='ajax_load_cities')

]
if  settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
    urlpatterns +=static(settings.MEDIA_URL,
                         document_root=settings.MEDIA_ROOT)
