"""mydjangoapp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
<<<<<<< HEAD
 i   https://docs.djangoproject.com/en/3.0/topics/http/urls/
=======
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
>>>>>>> 3a52be4fb20e7efe9ca22bad3b72580e849bd19b
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
<<<<<<< HEAD
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('quiz/', include('quiz.urls')),
=======
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
>>>>>>> 3a52be4fb20e7efe9ca22bad3b72580e849bd19b
]
