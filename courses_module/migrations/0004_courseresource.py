from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [("courses_module", "0003_alter_course_allowed_fields_and_more")]
    operations = [migrations.CreateModel(
        name="CourseResource",
        fields=[
            ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
            ("title", models.CharField(max_length=255, verbose_name="عنوان محتوا")),
            ("resource_type", models.CharField(choices=[("video", "ویدیو"), ("image", "تصویر"), ("pdf", "PDF")], max_length=10, verbose_name="نوع محتوا")),
            ("url", models.URLField(max_length=1000, verbose_name="لینک محتوا")),
            ("order", models.PositiveIntegerField(default=1, verbose_name="ترتیب نمایش")),
            ("is_active", models.BooleanField(default=True, verbose_name="فعال")),
            ("created_at", models.DateTimeField(auto_now_add=True)),
            ("course", models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name="resources", to="courses_module.course", verbose_name="دوره")),
        ],
        options={"ordering": ["order", "created_at"], "verbose_name": "محتوای دوره", "verbose_name_plural": "محتواهای دوره"},
    )]
