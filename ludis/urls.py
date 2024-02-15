from django.contrib import admin
from django.urls import path,include,re_path
from django.conf import settings
from django.views.static import serve
from django.conf.urls.static import static
from amharic import views
from django.contrib.sitemaps.views import sitemap
from repair.sitemaps import StaticSitemap
from django.views.generic.base import TemplateView

sitemaps = {
    'posts':StaticSitemap
}

admin.site.name = "Ludis"
admin.site.site_header = "Ludis Administration"

urlpatterns = [
    path('admin-ludis/', admin.site.urls),
    path('',include(('repair.urls','repair'),namespace='repair')),
    path('amh/',include('amharic.urls')),
    path(
        'sitemap.xml',sitemap,{'sitemaps':sitemaps},name='django.contrib.sitemaps.views.sitemap'
        ),
    re_path(r'^media/(?P<path>.*)$', serve,{'document_root': settings.MEDIA_ROOT}),
    re_path(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}),
    re_path(r'^ads\.txt$', views.googleadsense, name='google_adsense'),
    path('robots.txt', TemplateView.as_view(template_name='robots.txt', content_type='text/plain')),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)