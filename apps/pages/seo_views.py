from xml.etree.ElementTree import Element, SubElement, tostring
from django.http import HttpResponse
from django.urls import reverse
from django.views.decorators.http import require_GET

from .models import Project
from .views import ARTICLES


SITEMAP_PATHS = (
    ("pages:home", None),
    ("pages:projects", None),
    ("pages:articles", None),
    ("pages:about", None),
)


def _absolute_url(request, path):
    return request.build_absolute_uri(path)


@require_GET
def sitemap_xml(request):
    urlset = Element(
        "urlset",
        {"xmlns": "http://www.sitemaps.org/schemas/sitemap/0.9"},
    )

    for url_name, _ in SITEMAP_PATHS:
        loc = SubElement(urlset, "url")
        SubElement(
            loc,
            "loc",
        ).text = _absolute_url(request, reverse(url_name))

    for project in Project.objects.filter(is_published=True):
        entry = SubElement(urlset, "url")
        SubElement(
            entry,
            "loc",
        ).text = _absolute_url(
            request,
            reverse("pages:project_detail", kwargs={"slug": project.slug}),
        )
        SubElement(entry, "lastmod").text = project.updated_at.date().isoformat()

    for article in ARTICLES:
        entry = SubElement(urlset, "url")
        SubElement(
            entry,
            "loc",
        ).text = _absolute_url(
            request,
            reverse("pages:article_detail", kwargs={"slug": article["slug"]}),
        )
        SubElement(entry, "lastmod").text = article["date_iso"]

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
            f"Sitemap: {sitemap_url}",
            "",
        ]
    )
    return HttpResponse(body, content_type="text/plain; charset=utf-8")
