from django.urls import path
from apps.pages.views import HomeView, ComingSoonView

app_name = "pages"

urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    path("electronics/", ComingSoonView.as_view(page_title="بینوکس الکترونیک"), name="electronics"),
    path("articles/", ComingSoonView.as_view(page_title="مقاله‌های تکنولوژی"), name="articles"),
]
