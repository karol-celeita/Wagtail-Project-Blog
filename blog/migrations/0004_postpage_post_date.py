# Generated by Django 5.0.3 on 2024-03-12 03:52

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0003_postpage_body"),
    ]

    operations = [
        migrations.AddField(
            model_name="postpage",
            name="post_date",
            field=models.DateTimeField(
                default=datetime.datetime.today, verbose_name="post date"
            ),
        ),
    ]
