# Generated by Django 4.0.5 on 2022-06-13 21:56

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('institute', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course',
            name='duration',
        ),
        migrations.RemoveField(
            model_name='course',
            name='duration_unit',
        ),
        migrations.AddField(
            model_name='course',
            name='ends_at',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='course',
            name='starts_at',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='course',
            name='cover',
            field=models.ImageField(upload_to='institute/static/images/courses_img'),
        ),
    ]