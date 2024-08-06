"""Hello URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path
from home import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path("admin/",admin.site.urls),
    path("", views.signaction, name='signaction'),
    path("about",views.about, name='about'),
    path("error", views.error, name='error'),
    path("welcome",views.welcome, name='welcome'),
    path("signup_page", views.signup_page, name='signup_page'),
    path("my_maps", views.my_maps, name='my_maps'),
]