# Generated by Django 4.2.15 on 2024-08-14 09:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0002_videomodel_file_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='videomodel',
            name='full_name',
            field=models.TextField(default='none'),
        ),
        migrations.AddField(
            model_name='videomodel',
            name='status',
            field=models.TextField(default='none'),
        ),
        migrations.AddField(
            model_name='videomodel',
            name='username',
            field=models.TextField(default='none'),
        ),
    ]
