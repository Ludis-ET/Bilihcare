from django.contrib import sitemaps
from django.urls import reverse

class StaticSitemap(sitemaps.Sitemap):
    priority = 0.5
    changefreq = 'daily'
    
    def items(self):
        return [
            'repair:index',
            'repair:about',
            'repair:faq',
            'repair:login',
            'repair:terms',
            'repair:blog',
            'repair:apply',
            'repair:about',
        ]
    def location(self, item):
        return reverse(item)