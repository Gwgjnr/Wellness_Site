# Generated by Django 3.2 on 2022-06-24 12:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0003_contact_responded'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='responded',
            field=models.BooleanField(default=False),
        ),
    ]
