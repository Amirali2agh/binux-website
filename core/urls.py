from django.conf import settings
from django.contrib import admin
from django.urls import include, path, re_path
from django.views.static import serve

from apps.pages.seo_views import robots_txt, sitemap_xml

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('apps.pages.urls', namespace='pages')),
    path('sitemap.xml', sitemap_xml, name='sitemap'),
    path('robots.txt', robots_txt, name='robots'),
]

# Portfolio uploads are public by design; production reverse proxies can serve /media/ directly later.
urlpatterns += [re_path(r"^media/(?P<path>.*)$", serve, {"document_root": settings.MEDIA_ROOT})]
