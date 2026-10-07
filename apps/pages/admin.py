from django.contrib import admin
from django.utils.html import format_html

from .models import Project, ProjectImage


class ProjectImageInline(admin.TabularInline):
    model = ProjectImage
    extra = 1
    fields = ("image", "preview", "alt_text", "caption", "sort_order", "is_active")
    readonly_fields = ("preview",)
    ordering = ("sort_order", "id")

    @admin.display(description="پیش‌نمایش")
    def preview(self, obj):
        if not obj.pk or not obj.image:
            return "—"
        try:
            return format_html(
                '<img src="{}" alt="{}" style="width:120px;height:72px;object-fit:cover;border-radius:10px;border:1px solid #334155;" />',
                obj.image.url,
                obj.alt_text or obj.caption or obj.project.title,
            )
        except ValueError:
            return "—"


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "category",
        "is_published",
        "is_featured",
        "sort_order",
        "gallery_count",
        "updated_at",
    )
    list_filter = ("is_published", "is_featured", "category")
    search_fields = ("title", "category", "short_description", "description", "technologies")
    prepopulated_fields = {"slug": ("title",)}
    ordering = ("sort_order", "-updated_at")
    list_editable = ("is_published", "is_featured", "sort_order")
    readonly_fields = ("created_at", "updated_at")
    fieldsets = (
        (
            "اطلاعات اصلی",
            {
                "fields": (
                    "title",
                    "slug",
                    "category",
                    "short_description",
                    "description",
                    "technologies",
                )
            },
        ),
        (
            "رسانه و لینک",
            {
                "fields": (
                    "cover_image",
                    "project_url",
                    "project_url_label",
                )
            },
        ),
        (
            "نمایش",
            {
                "fields": (
                    "is_published",
                    "is_featured",
                    "sort_order",
                )
            },
        ),
        (
            "اطلاعات سیستمی",
            {
                "fields": (
                    "created_at",
                    "updated_at",
                ),
                "classes": ("collapse",),
            },
        ),
    )
    inlines = [ProjectImageInline]

    @admin.display(description="تعداد تصاویر")
    def gallery_count(self, obj):
        return obj.gallery.filter(is_active=True).count()


@admin.register(ProjectImage)
class ProjectImageAdmin(admin.ModelAdmin):
    list_display = ("project", "preview", "caption", "sort_order", "is_active")
    list_filter = ("is_active", "project")
    search_fields = ("project__title", "caption", "alt_text")
    list_editable = ("sort_order", "is_active")
    autocomplete_fields = ("project",)
    fields = ("project", "image", "preview", "alt_text", "caption", "sort_order", "is_active")
    readonly_fields = ("preview",)
    ordering = ("project", "sort_order", "id")

    @admin.display(description="پیش‌نمایش")
    def preview(self, obj):
        if not obj.pk or not obj.image:
            return "—"
        try:
            return format_html(
                '<img src="{}" alt="{}" style="width:180px;height:105px;object-fit:cover;border-radius:12px;border:1px solid #334155;" />',
                obj.image.url,
                obj.alt_text or obj.caption or obj.project.title,
            )
        except ValueError:
            return "—"
