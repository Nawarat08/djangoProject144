from django.contrib import admin
from django.urls import path, include
from ProfileApp import view

urlpatterns = [
    path('', view.home, name='home'),
    path('admin/', admin.site.urls),
    path('ProfileApp/', include('ProfileApp.urls'))
]
