# Generated by Django 2.2.7 on 2019-11-30 05:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0002_auto_20191130_0430'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='attachment',
            field=models.FileField(blank=True, upload_to='', verbose_name='첨부파일'),
        ),
    ]