# Generated by Django 5.1.1 on 2024-10-07 12:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_userprofile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='post_code',
            field=models.CharField(blank=True, max_length=7, null=True),
        ),
    ]
