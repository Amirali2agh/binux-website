from django.views.generic import TemplateView

class HomeView(TemplateView):
    template_name = "pages/home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["seo_title"] = "طراحی سایت حرفه‌ای برای رشد واقعی کسب‌وکار شما | نادرو استودیو"
        context["seo_description"] = "خدمات تخصصی طراحی سایت مدرن، بهینه‌سازی شده برای گوگل (SEO) و توسعه متمرکز بر تجربه کاربری برای رشد کسب‌وکار شما."
        context["seo_keywords"] = "طراحی وب سایت, طراحی سایت جنگو, سئو سایت, نادرو استودیو"
        context["canonical_url"] = self.request.build_absolute_uri('/')
        return context
