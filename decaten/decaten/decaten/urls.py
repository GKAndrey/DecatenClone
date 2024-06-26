"""
URL configuration for decaten project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from decaten.settings import DEBUG, MEDIA_URL, MEDIA_ROOT
from django.conf.urls.static import static
from main.views import main
from base.views import base
from user.views import log_page, reg_page,logout_page, validate_account, log_in_account

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', main, name='main'),
    path('base/', base, name='base'),
    path('login/', log_page, name='log'),
    path('registration/', reg_page, name='reg'),
    path('logout', logout_page, name='logout'),
    path('validate_account/', validate_account, name='validate_account'),
    path('log_in_account/', log_in_account, name='log_in_account')
]

if DEBUG:
    urlpatterns += static(MEDIA_URL, document_root=MEDIA_ROOT)