from django.contrib.sitemaps import Sitemap
from .models import Content, Creator


class ContentSiteMap(Sitemap):
    changefreq = 'daily'
    priority = 0.9
    def items(self):
        return Content.objects.all()
    
    def lastmod(self, obj):
        return obj.date_uploaded


class CreatorSiteMap(Sitemap):
    changefreq = 'daily'
    priority = 0.9
    def items(self):
        return Creator.objects.all()
    
    def lastmod(self, obj):
        return obj.date_joined