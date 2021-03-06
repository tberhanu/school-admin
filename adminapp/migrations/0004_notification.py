# Generated by Django 2.0 on 2018-11-04 06:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('adminapp', '0003_auto_20181103_1927'),
    ]

    operations = [
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
                ('level', models.CharField(blank=True, max_length=30)),
                ('content', models.TextField(blank=True, max_length=500)),
                ('image', models.ImageField(blank=True, upload_to='notification_image')),
                ('pub_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(auto_now=True)),
                ('course', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='adminapp.Subject')),
                ('poster', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='adminapp.Teacher')),
            ],
        ),
    ]
