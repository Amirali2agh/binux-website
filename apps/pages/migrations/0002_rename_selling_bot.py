from django.db import migrations


def rename_config_selling_bots(apps, schema_editor):
    Project = apps.get_model("pages", "Project")
    Project.objects.filter(slug="config-selling-bots").update(title="Selling Bot")


def restore_config_selling_bots(apps, schema_editor):
    Project = apps.get_model("pages", "Project")
    Project.objects.filter(slug="config-selling-bots").update(title="Config Selling Bots")


class Migration(migrations.Migration):
    dependencies = [
        ("pages", "0001_initial"),
    ]

    operations = [
        migrations.RunPython(rename_config_selling_bots, restore_config_selling_bots),
    ]
