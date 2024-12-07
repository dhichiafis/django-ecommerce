# Generated by Django 5.1.4 on 2024-12-07 06:36

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Movie",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("title", models.CharField(max_length=255)),
                ("description", models.TextField()),
                ("image", models.ImageField(upload_to="media")),
            ],
        ),
    ]
