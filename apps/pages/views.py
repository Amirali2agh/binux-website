from django.views.generic import TemplateView

class HomeView(TemplateView):
    template_name = "pages/home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["seo_title"] = "طراحی سایت‌های پیشرفته با بینوکس (Binux) | بهینه‌سازی شده برای گوگل"
        context["seo_description"] = "آژانس دیجیتال بینوکس (Binux) ارائه دهنده خدمات طراحی سایت مدرن با جنگو، متمرکز بر سرعت بی‌نظیر و سئوی حداکثری."
        context["seo_keywords"] = "بینوکس, Binux, طراحی وب سایت, سئو سایت, جنگو لینوکس"
        context["canonical_url"] = self.request.build_absolute_uri('/')
        return context

class ComingSoonView(TemplateView):
    template_name = "pages/coming_soon.html"
    page_title = ""

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["page_title"] = self.page_title
        context["seo_title"] = f"{self.page_title} | به زودی در بینوکس"
        context["seo_description"] = "این صفحه در حال حاضر در دست توسعه و طراحی زیرساخت پایتون/جنگو است و به زودی منتشر خواهد شد."
        context["canonical_url"] = self.request.build_absolute_uri(self.request.path)
        return context
