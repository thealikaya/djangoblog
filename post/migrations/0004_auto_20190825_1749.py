# Generated by Django 2.2.4 on 2019-08-25 14:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0003_auto_20190825_1613'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='content',
            field=models.TextField(verbose_name='İçerik'),
        ),
    ]
