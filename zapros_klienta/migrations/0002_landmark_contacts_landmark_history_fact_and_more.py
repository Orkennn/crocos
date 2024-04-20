# Generated by Django 4.2.11 on 2024-04-20 13:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zapros_klienta', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='landmark',
            name='contacts',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='landmark',
            name='history_fact',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='landmark',
            name='price',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='landmark',
            name='work_schedule',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]