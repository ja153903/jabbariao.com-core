# Generated by Django 3.2.4 on 2021-08-22 22:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("posts", "0004_auto_20210822_2016"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="tag",
            name="posts",
        ),
    ]
