from xml.etree.ElementTree import Element, SubElement, tostring

from django.http import HttpResponse
from django.urls import reverse
from django.views.decorators.http import require_GET

from .models import Project
from .services import SERVICES
from .views import ARTICLES


# (url name, changefreq, priority)
SITEMAP_PATHS = (
    ("pages:home", "weekly", "1.0"),
    ("pages:services", "monthly", "0.9"),
    ("pages:projects", "weekly", "0.8"),
    ("pages:articles", "weekly", "0.8"),
    ("pages:about", "monthly", "0.6"),
)


def _absolute_url(request, path):
    return request.build_absolute_uri(path)


def _append_url(urlset, request, path, lastmod=None, changefreq=None, priority=None):
    entry = SubElement(urlset, "url")
    SubElement(entry, "loc").text = _absolute_url(request, path)
    if lastmod:
        SubElement(entry, "lastmod").text = lastmod
    if changefreq:
        SubElement(entry, "changefreq").text = changefreq
    if priority:
        SubElement(entry, "priority").text = priority
    return entry


@require_GET
def sitemap_xml(request):
    urlset = Element(
        "urlset",
        {"xmlns": "http://www.sitemaps.org/schemas/sitemap/0.9"},
    )

    for url_name, changefreq, priority in SITEMAP_PATHS:
        _append_url(
            urlset,
            request,
            reverse(url_name),
            changefreq=changefreq,
            priority=priority,
        )

    # Service landing pages are the primary organic entry points for the
    # commercial keywords, so they sit just below the homepage in priority.
    for service in SERVICES:
        _append_url(
            urlset,
            request,
            reverse("pages:service_detail", kwargs={"slug": service["slug"]}),
            changefreq="monthly",
            priority="0.9",
        )

    for project in Project.objects.filter(is_published=True):
        _append_url(
            urlset,
            request,
            reverse("pages:project_detail", kwargs={"slug": project.slug}),
            lastmod=project.updated_at.date().isoformat(),
            changefreq="monthly",
            priority="0.7",
        )

    for article in ARTICLES:
        _append_url(
            urlset,
            request,
            reverse("pages:article_detail", kwargs={"slug": article["slug"]}),
            lastmod=article["date_iso"],
            changefreq="monthly",
            priority="0.6",
        )

    xml = tostring(urlset, encoding="utf-8", xml_declaration=True)
    return HttpResponse(xml, content_type="application/xml; charset=utf-8")


@require_GET
def robots_txt(request):
    sitemap_url = _absolute_url(request, "/sitemap.xml")
    body = "\n".join(
        [
            "User-agent: *",
            "Allow: /",
            "Disallow: /admin/",
            "Disallow: /deploy-init/",
            "",
            f"Sitemap: {sitemap_url}",
            "",
        ]
    )
    return HttpResponse(body, content_type="text/plain; charset=utf-8")
