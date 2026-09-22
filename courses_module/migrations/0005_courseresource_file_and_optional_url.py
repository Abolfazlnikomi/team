from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [("courses_module", "0004_courseresource")]

    operations = [
        migrations.AddField(
            model_name="courseresource",
            name="file",
            field=models.FileField(blank=True, upload_to="courses/resources/", verbose_name="فایل محتوا"),
        ),
        migrations.AlterField(
            model_name="courseresource",
            name="url",
            field=models.URLField(blank=True, max_length=1000, verbose_name="لینک محتوا"),
        ),
    ]
