# Generated by Django 2.1 on 2018-11-17 12:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fisica', '0003_auto_20181117_1311'),
    ]

    operations = [
        migrations.AlterField(
            model_name='misurazione',
            name='media',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=3, null=True),
        ),
    ]
