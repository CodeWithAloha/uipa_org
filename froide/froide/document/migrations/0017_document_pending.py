# Generated by Django 2.1.9 on 2019-08-15 08:47

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("document", "0016_auto_20190806_2121"),
    ]

    operations = [
        migrations.AddField(
            model_name="document",
            name="pending",
            field=models.BooleanField(default=False),
        ),
    ]