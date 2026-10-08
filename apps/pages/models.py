from django.core.validators import FileExtensionValidator
from django.db import models
from django.urls import reverse


IMAGE_EXTENSIONS = ["jpg", "jpeg", "png", "webp", "gif", "svg"]


class Project(models.Model):
    title = models.CharField("عنوان پروژه", max_length=180)
    slug = models.SlugField("شناسه یکتا", max_length=190, unique=True)
    category = models.CharField("دسته‌بندی", max_length=120)
    short_description = models.CharField("توضیح کوتاه", max_length=320)
    description = models.TextField("توضیحات کامل")
    technologies = models.CharField(
        "فناوری‌ها",
        max_length=500,
        help_text="فناوری‌ها را با کاما انگلیسی جدا کنید؛ مثال: Django, React, PostgreSQL",
    )
    cover_image = models.FileField(
        "تصویر شاخص",
        upload_to="projects/covers/",
        blank=True,
        null=True,
        validators=[FileExtensionValidator(allowed_extensions=IMAGE_EXTENSIONS)],
    )
    project_url = models.URLField("لینک پروژه", blank=True)
    project_url_label = models.CharField("متن لینک پروژه", max_length=80, blank=True)
    is_published = models.BooleanField("نمایش در سایت", default=True)
    is_featured = models.BooleanField("نمایش در صفحه اصلی", default=True)
    sort_order = models.PositiveIntegerField("ترتیب نمایش", default=0)
    created_at = models.DateTimeField("تاریخ ایجاد", auto_now_add=True)
    updated_at = models.DateTimeField("آخرین بروزرسانی", auto_now=True)

    class Meta:
        ordering = ["sort_order", "-created_at"]
        verbose_name = "پروژه"
        verbose_name_plural = "پروژه‌ها"

    def __str__(self):
        return self.title

    @property
    def technology_list(self):
        return [item.strip() for item in self.technologies.split(",") if item.strip()]

    def get_absolute_url(self):
        return reverse("pages:project_detail", kwargs={"slug": self.slug})


class ProjectImage(models.Model):
    project = models.ForeignKey(
        Project,
        on_delete=models.CASCADE,
        related_name="gallery",
        verbose_name="پروژه",
    )
    image = models.FileField(
        "تصویر",
        upload_to="projects/gallery/",
        validators=[FileExtensionValidator(allowed_extensions=IMAGE_EXTENSIONS)],
    )
    alt_text = models.CharField("متن جایگزین", max_length=220, blank=True)
    caption = models.CharField("عنوان تصویر", max_length=220, blank=True)
    sort_order = models.PositiveIntegerField("ترتیب نمایش", default=0)
    is_active = models.BooleanField("نمایش تصویر", default=True)

    class Meta:
        ordering = ["sort_order", "id"]
        verbose_name = "تصویر پروژه"
        verbose_name_plural = "آلبوم تصاویر پروژه"

    def __str__(self):
        return self.caption or f"{self.project.title} #{self.pk}"
