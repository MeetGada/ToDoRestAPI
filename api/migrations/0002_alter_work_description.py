# Generated by Django 4.0 on 2022-01-21 17:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='work',
            name='description',
            field=models.TextField(blank=True, default=None, max_length=200, null=True),
        ),
    ]
