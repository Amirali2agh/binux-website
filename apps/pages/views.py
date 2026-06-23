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

class ElectronicsView(TemplateView):
    template_name = "pages/electronics.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["seo_title"] = "بینوکس الکترونیک | آزمایشگاه توسعه سخت‌افزار"
        context["seo_description"] = "بخش مهندسی الکترونیک و اینترنت اشیاء (IoT) گروه بینوکس. به زودی از پلتفرم جدید سخت‌افزاری رونمایی خواهد شد."
        context["canonical_url"] = self.request.build_absolute_uri(self.request.path)
        return context

class ArticlesView(TemplateView):
    template_name = "pages/articles.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["seo_title"] = "مقاله‌های تکنولوژی | وبلاگ فنی بینوکس"
        context["seo_description"] = "مجموعه مقالات و آموزش‌های تخصصی برنامه‌نویسی پایتون، فریم‌ورک جنگو، توسعه لینوکس و استانداردهای سئو."
        context["canonical_url"] = self.request.build_absolute_uri(self.request.path)
        
        # Real-world Persian SEO Optimized tech articles data
        context["articles"] = [
            {
                "title": "چگونه سرعت لود جنگو را در سرور اوبونتو به زیر ۲۰۰ میلی‌ثانیه برسانیم؟",
                "summary": "بررسی جامع متدهای بهینه‌سازی کوئری‌های دیتابیس، کش کردن با Redis، فشرده‌سازی با Gzip و تنظیمات بهینه وب‌سرور Nginx برای سرعت‌های نجومی.",
                "date": "۲ تیر ۱۴۰۵",
                "read_time": "۵ دقیقه مطالعه",
                "category": "جنگو و سرور"
            },
            {
                "title": "استاندارد داده‌های ساختاریافته (JSON-LD) و جادوی آن در رتبه‌بندی محلی گوگل",
                "summary": "چگونه با تزریق کدهای معنایی ساختاریافته به موتورهای جستجو بفهمانیم که شرکت ما کجاست، چه ساعاتی کار می‌کند و پلتفرم ما چقدر معتبر است.",
                "date": "۲۸ خرداد ۱۴۰۵",
                "read_time": "۷ دقیقه مطالعه",
                "category": "سئو و بهینه‌سازی"
            },
            {
                "title": "راهنمای ورود به دنیای لینوکس از طریق ویندوز با کیت توسعه WSL2",
                "summary": "بررسی مزیت‌ها و چالش‌های اجرای توزیع اوبونتو روی WSL ویندوز به همراه پیکربندی پایدار داکر برای شبیه‌سازی دقیق سرورهای پروداکشن.",
                "date": "۱۵ خرداد ۱۴۰۵",
                "read_time": "۴ دقیقه مطالعه",
                "category": "لینوکس و توسعه"
            }
        ]
        return context

class AboutView(TemplateView):
    template_name = "pages/about.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["seo_title"] = "درباره ما | گروه فناوری و آژانس دیجیتال بینوکس"
        context["seo_description"] = "آشنایی با تیم فنی بینوکس، اطلاعات تماس، آدرس پیج اینستاگرام، کانال تلگرام، ایمیل پشتیبانی و اینماد بینوکس."
        context["canonical_url"] = self.request.build_absolute_uri(self.request.path)
        return context
