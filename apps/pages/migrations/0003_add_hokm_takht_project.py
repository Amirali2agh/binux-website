from django.db import migrations


def add_hokm_takht_project(apps, schema_editor):
    Project = apps.get_model("pages", "Project")
    Project.objects.update_or_create(
        slug="hokm-takht",
        defaults={
            "title": "بازی آنلاین حکم و تخته‌نرد",
            "category": "بازی‌های آنلاین و Real-Time",
            "short_description": (
                "طراحی بک‌اند بازی‌های آنلاین حکم و تخته‌نرد با Matchmaking، "
                "وضعیت زنده بازی و ارتباط بلادرنگ مبتنی بر WebSocket."
            ),
            "description": (
                "یک مجموعه بازی آنلاین مبتنی بر معماری Real-Time که برای دو بازی حکم و تخته‌نرد توسعه داده شده است. "
                "بخش حکم یک بازی چهار نفره دو به دو را با مدیریت صف Matchmaking، ساخت اتاق بازی، چرخش حاکم، "
                "بررسی قوانین رعایت خال و امتیازدهی بازی مدیریت می‌کند. "
                "در بخش تخته‌نرد نیز لابی و Matchmaking، اتاق بازی، وضعیت کامل صفحه و مهره‌ها، تاس، حرکت مهره‌ها، "
                "Bar و Bearing Off، کنترل زمان نوبت و مدیریت قطع و اتصال مجدد بازیکنان پیاده‌سازی شده است. "
                "هر دو سرویس با FastAPI، Redis و WebSockets برای ارتباط کم‌تاخیر و مدیریت وضعیت زنده طراحی شده‌اند "
                "و با Docker قابل اجرا و استقرار هستند."
            ),
            "technologies": (
                "Python, FastAPI, Redis, WebSockets, Docker, Docker Compose, "
                "Real-Time Systems, Matchmaking"
            ),
            "project_url": "",
            "project_url_label": "",
            "is_published": True,
            "is_featured": True,
            "sort_order": 5,
        },
    )


def remove_hokm_takht_project(apps, schema_editor):
    Project = apps.get_model("pages", "Project")
    Project.objects.filter(slug="hokm-takht").delete()


class Migration(migrations.Migration):
    dependencies = [
        ("pages", "0002_rename_selling_bot"),
    ]

    operations = [
        migrations.RunPython(add_hokm_takht_project, remove_hokm_takht_project),
    ]
