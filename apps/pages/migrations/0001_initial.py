from django.db import migrations, models
import django.core.validators
import django.db.models.deletion


def seed_projects(apps, schema_editor):
    Project = apps.get_model("pages", "Project")

    projects = [
        {
            "title": "Meshcat ERP",
            "slug": "meshcat-erp",
            "category": "سامانه یکپارچه مدیریت سازمانی",
            "short_description": "ERP اختصاصی برای مدیریت یکپارچه فروش، قراردادها، امور مالی، عملیات و فرآیندهای سازمانی.",
            "description": (
                "طراحی و توسعه یک ERP اختصاصی برای یکپارچه‌سازی فرآیندهای فروش، مدیریت مشتریان، "
                "رسانه و دارایی‌ها، قراردادها، امور مالی، عملیات، امور حقوقی و مدیریت داخلی سازمان. "
                "این سامانه با معماری ماژولار و رابط کاربری فارسی و راست‌چین، برای استفاده روزمره تیم‌های سازمانی طراحی شده است."
            ),
            "technologies": "Django, Django REST Framework, React, TypeScript, Vite, Tailwind CSS, Docker, REST API",
            "project_url": "",
            "project_url_label": "",
            "is_published": True,
            "is_featured": True,
            "sort_order": 1,
        },
        {
            "title": "Komak Moshaver",
            "slug": "komak-moshaver",
            "category": "CRM و سامانه مدیریت املاک",
            "short_description": "CRM اختصاصی برای مدیریت مشتریان، فایل‌های ملکی، مشاوران و فرآیندهای فروش با امکانات مکانی و داشبورد مدیریتی.",
            "description": (
                "طراحی و توسعه یک CRM تخصصی برای کسب‌وکارهای حوزه املاک با تمرکز بر مدیریت مشتریان، "
                "فایل‌های ملکی، مشاوران و عملیات فروش. این محصول از داشبوردهای مدیریتی، جست‌وجوی مکانی، "
                "نقشه و زیرساخت آماده برای قابلیت‌های هوشمند پشتیبانی می‌کند."
            ),
            "technologies": "Django, Django REST Framework, React, Vite, Tailwind CSS, PostgreSQL, Redis, Maps",
            "project_url": "",
            "project_url_label": "",
            "is_published": True,
            "is_featured": True,
            "sort_order": 2,
        },
        {
            "title": "Config Selling Bots",
            "slug": "config-selling-bots",
            "category": "پلتفرم فروش و اتوماسیون سرویس",
            "short_description": "پلتفرم فروش خودکار سرویس‌های دیجیتال با سفارش، پرداخت، کیف پول، اشتراک و پردازش‌های پس‌زمینه.",
            "description": (
                "توسعه یک پلتفرم ماژولار فروش سرویس‌های دیجیتال با Django که بخش فروش، سفارش، پرداخت، "
                "کیف پول، ارجاع، OTP، موجودی سرویس و چرخه عمر اشتراک را یکپارچه می‌کند. "
                "اتصال ربات تلگرام و پردازش‌های پس‌زمینه با Celery و Redis، بخش مهمی از معماری اتوماسیون این پروژه است."
            ),
            "technologies": "Django, PostgreSQL, Redis, Celery, Docker, Telegram Bot, REST API",
            "project_url": "",
            "project_url_label": "",
            "is_published": True,
            "is_featured": True,
            "sort_order": 3,
        },
        {
            "title": "Speed Service",
            "slug": "speed-service",
            "category": "وب‌سایت تعاملی خدمات شبکه و زیرساخت",
            "short_description": "وب‌سایت سینمایی و تعاملی برای خدمات شبکه و زیرساخت با تجربه بصری مبتنی بر WebGL و انیمیشن.",
            "description": (
                "طراحی و توسعه یک وب‌سایت مدرن برای معرفی خدمات شبکه و زیرساخت با تمرکز بر تجربه بصری. "
                "این پروژه از React، Three.js، React Three Fiber و GSAP برای ساخت پس‌زمینه تعاملی WebGL، "
                "حرکت‌های سینمایی و تجربه اسکرول‌محور استفاده می‌کند."
            ),
            "technologies": "React, Vite, Three.js, React Three Fiber, WebGL, GSAP, Tailwind CSS",
            "project_url": "https://github.com/Amirali2agh/speed-site",
            "project_url_label": "مشاهده پروژه عمومی",
            "is_published": True,
            "is_featured": True,
            "sort_order": 4,
        },
    ]

    for payload in projects:
        Project.objects.update_or_create(slug=payload["slug"], defaults=payload)


def unseed_projects(apps, schema_editor):
    Project = apps.get_model("pages", "Project")
    Project.objects.filter(
        slug__in=[
            "meshcat-erp",
            "komak-moshaver",
            "config-selling-bots",
            "speed-service",
        ]
    ).delete()


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Project",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("title", models.CharField(max_length=180, verbose_name="عنوان پروژه")),
                ("slug", models.SlugField(max_length=190, unique=True, verbose_name="شناسه یکتا")),
                ("category", models.CharField(max_length=120, verbose_name="دسته‌بندی")),
                ("short_description", models.CharField(max_length=320, verbose_name="توضیح کوتاه")),
                ("description", models.TextField(verbose_name="توضیحات کامل")),
                (
                    "technologies",
                    models.CharField(
                        help_text="فناوری‌ها را با کاما انگلیسی جدا کنید؛ مثال: Django, React, PostgreSQL",
                        max_length=500,
                        verbose_name="فناوری‌ها",
                    ),
                ),
                (
                    "cover_image",
                    models.FileField(
                        blank=True,
                        null=True,
                        upload_to="projects/covers/",
                        validators=[
                            django.core.validators.FileExtensionValidator(
                                allowed_extensions=["jpg", "jpeg", "png", "webp", "gif", "svg"]
                            )
                        ],
                        verbose_name="تصویر شاخص",
                    ),
                ),
                ("project_url", models.URLField(blank=True, verbose_name="لینک پروژه")),
                ("project_url_label", models.CharField(blank=True, max_length=80, verbose_name="متن لینک پروژه")),
                ("is_published", models.BooleanField(default=True, verbose_name="نمایش در سایت")),
                ("is_featured", models.BooleanField(default=True, verbose_name="نمایش در صفحه اصلی")),
                ("sort_order", models.PositiveIntegerField(default=0, verbose_name="ترتیب نمایش")),
                ("created_at", models.DateTimeField(auto_now_add=True, verbose_name="تاریخ ایجاد")),
                ("updated_at", models.DateTimeField(auto_now=True, verbose_name="آخرین بروزرسانی")),
            ],
            options={
                "verbose_name": "پروژه",
                "verbose_name_plural": "پروژه‌ها",
                "ordering": ["sort_order", "-created_at"],
            },
        ),
        migrations.CreateModel(
            name="ProjectImage",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                (
                    "image",
                    models.FileField(
                        upload_to="projects/gallery/",
                        validators=[
                            django.core.validators.FileExtensionValidator(
                                allowed_extensions=["jpg", "jpeg", "png", "webp", "gif", "svg"]
                            )
                        ],
                        verbose_name="تصویر",
                    ),
                ),
                ("alt_text", models.CharField(blank=True, max_length=220, verbose_name="متن جایگزین")),
                ("caption", models.CharField(blank=True, max_length=220, verbose_name="عنوان تصویر")),
                ("sort_order", models.PositiveIntegerField(default=0, verbose_name="ترتیب نمایش")),
                ("is_active", models.BooleanField(default=True, verbose_name="نمایش تصویر")),
                (
                    "project",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="gallery",
                        to="pages.project",
                        verbose_name="پروژه",
                    ),
                ),
            ],
            options={
                "verbose_name": "تصویر پروژه",
                "verbose_name_plural": "آلبوم تصاویر پروژه",
                "ordering": ["sort_order", "id"],
            },
        ),
        migrations.RunPython(seed_projects, unseed_projects),
    ]
