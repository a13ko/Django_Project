# Generated by Django 4.1.7 on 2023-02-28 18:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_profile_activation_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='activation_code',
            field=models.CharField(blank=True, max_length=200, null=True, unique=True),
        ),
    ]