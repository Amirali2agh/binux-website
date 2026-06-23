from django.urls import path
from apps.pages.views import HomeView, ElectronicsView, ArticlesView, AboutView

app_name = "pages"

urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    path("electronics/", ElectronicsView.as_view(), name="electronics"),
    path("articles/", ArticlesView.as_view(), name="articles"),
    path("about/", AboutView.as_view(), name="about"),
]
