from django.db import migrations


def add_realtime_chat_project(apps, schema_editor):
    Project = apps.get_model("pages", "Project")
    Project.objects.update_or_create(
        slug="realtime-chat-social",
        defaults={
            "title": "پلتفرم چت و شبکه اجتماعی Real-Time",
            "category": "پیام‌رسان و شبکه اجتماعی",
            "short_description": (
                "پلتفرم ارتباطی بلادرنگ با چت خصوصی و گروهی، ساخت کانال، تماس تصویری، لایو، "
                "استوری و سیستم دنبال‌کردن کاربران."
            ),
            "description": (
                "طراحی و توسعه یک پلتفرم ارتباطی و شبکه اجتماعی با محوریت ارتباطات Real-Time و تجربه کاربری یکپارچه. "
                "این سامانه علاوه بر گفت‌وگوی خصوصی، امکان ایجاد گروه و کانال، مدیریت ارتباطات اجتماعی و "
                "سیستم Follow / Unfollow کاربران را فراهم می‌کند. قابلیت‌های محتوایی مانند Story و Live نیز "
                "برای تعامل سریع و انتشار محتوای موقت و زنده در نظر گرفته شده‌اند. "
                "بخش ارتباطات بلادرنگ با WebSocket پیاده‌سازی شده تا پیام‌ها و رویدادهای تعاملی بدون نیاز به polling "
                "میان کاربران و سرور منتقل شوند. تماس تصویری نیز به‌عنوان بخشی از تجربه ارتباطی پلتفرم در کنار "
                "لایه Real-Time طراحی شده است. معماری پروژه برای مدیریت همزمانی، اتاق‌های ارتباطی، رویدادهای زنده، "
                "حضور کاربران و رشد تعداد کاربران طراحی شده و قابلیت توسعه به امکانات اجتماعی و ارتباطی بیشتر را دارد."
            ),
            "technologies": (
                "Python, Django, WebSockets, Real-Time Communication, "
                "Video Calling, Social Network, REST API"
            ),
            "project_url": "",
            "project_url_label": "",
            "is_published": True,
            "is_featured": True,
            "sort_order": 6,
        },
    )


def remove_realtime_chat_project(apps, schema_editor):
    Project = apps.get_model("pages", "Project")
    Project.objects.filter(slug="realtime-chat-social").delete()


class Migration(migrations.Migration):
    dependencies = [
        ("pages", "0003_add_hokm_takht_project"),
    ]

    operations = [
        migrations.RunPython(add_realtime_chat_project, remove_realtime_chat_project),
    ]
