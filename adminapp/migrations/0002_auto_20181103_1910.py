# Generated by Django 2.0 on 2018-11-04 02:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='parent',
            name='picture',
            field=models.ImageField(blank=True, upload_to='profile_image'),
        ),
        migrations.AddField(
            model_name='student',
            name='picture',
            field=models.ImageField(blank=True, upload_to='profile_image'),
        ),
        migrations.AddField(
            model_name='teacher',
            name='picture',
            field=models.ImageField(blank=True, upload_to='profile_image'),
        ),
    ]
