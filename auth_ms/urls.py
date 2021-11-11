from django.contrib import admin
from django.urls import path,include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('rest-auth/',include('rest_auth.urls')),#Primero recibe una url, luego se coloca hacia donde se dirige y por ultimo el include permite importar los metodos de la lbreria  
    path('rest-auth/registration',include('rest_auth.registration.urls'))
]
    