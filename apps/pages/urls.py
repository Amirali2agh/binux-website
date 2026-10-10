from django.urls import path

from apps.pages.views import (
    AboutView,
    ArticleDetailView,
    ArticlesView,
    ElectronicsView,
    HomeView,
    ProjectDetailView,
    ProjectsView,
    ServiceDetailView,
    ServicesView,
)

app_name = "pages"

urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    path("services/", ServicesView.as_view(), name="services"),
    path("services/<slug:slug>/", ServiceDetailView.as_view(), name="service_detail"),
    path("projects/", ProjectsView.as_view(), name="projects"),
    path("projects/<slug:slug>/", ProjectDetailView.as_view(), name="project_detail"),
    path("electronics/", ElectronicsView.as_view(), name="electronics"),
    path("articles/", ArticlesView.as_view(), name="articles"),
    path("articles/<slug:slug>/", ArticleDetailView.as_view(), name="article_detail"),
    path("about/", AboutView.as_view(), name="about"),
]
