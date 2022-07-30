# Generated by Django 3.2 on 2022-07-30 20:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('virtual_sessions', '0002_auto_20220624_1204'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='session',
            options={'ordering': ['-created_date']},
        ),
        migrations.RemoveField(
            model_name='session',
            name='category',
        ),
        migrations.RemoveField(
            model_name='session',
            name='number_of_sessions',
        ),
        migrations.RemoveField(
            model_name='session',
            name='price',
        ),
        migrations.AddField(
            model_name='session',
            name='slug',
            field=models.SlugField(max_length=200, null=True, unique=True),
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('body', models.TextField()),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('approved', models.BooleanField(default=True)),
                ('reply', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='replies', to='virtual_sessions.comment')),
                ('session', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='virtual_sessions.session')),
            ],
            options={
                'ordering': ['created_on'],
            },
        ),
    ]
