"""Codectionary URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path, include, re_path
from django.views.generic import TemplateView
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.sitemaps.views import sitemap
from codectionaryapp.sitemaps import ContentSiteMap, CreatorSiteMap
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.views.static import serve

sitemaps = {
    'contents' : ContentSiteMap,
    'creator' : CreatorSiteMap,
}

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('codectionaryapp.urls')),
    path('accounts/',include('allauth.urls')),
    path(
        'sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'
    ),
    re_path(r'^media/(?P<path>.*)$', serve,{'document_root': settings.MEDIA_ROOT})


]

urlpatterns += staticfiles_urlpatterns()