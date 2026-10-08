from django.urls import path

from apps.pages.views import (
    AboutView,
    ArticleDetailView,
    ArticlesView,
    ElectronicsView,
    HomeView,
    ProjectDetailView,
    ProjectsView,
)

app_name = "pages"

urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    path("projects/", ProjectsView.as_view(), name="projects"),
    path("projects/<slug:slug>/", ProjectDetailView.as_view(), name="project_detail"),
    path("electronics/", ElectronicsView.as_view(), name="electronics"),
    path("articles/", ArticlesView.as_view(), name="articles"),
    path("articles/<slug:slug>/", ArticleDetailView.as_view(), name="article_detail"),
    path("about/", AboutView.as_view(), name="about"),
]
